#!/usr/bin/env python3
"""AD&C private-friendly, static HTML report renderer (Python stdlib only).

Usage: python render_report.py input.json output.html
The caller retrieves authorized source records and produces input.json.
This tool does NOT fetch, publish, send, schedule, or update any service.
"""
import argparse
import html
import json
from pathlib import Path
from urllib.parse import urlsplit

KIND_NAMES = {'secretary': '秘書', 'project': 'PJ', 'routine': '定例タスク'}
PRIORITIES = {'P0', 'P1', 'P2', 'OTHER'}


def h(value):
    return html.escape('' if value is None else str(value), quote=True)


def approved_href(value):
    """Only literal HTTPS links; URL text is not used to construct scripts."""
    if not isinstance(value, str) or not value:
        return ''
    try:
        p = urlsplit(value)
        if p.scheme.lower() != 'https' or not p.hostname or p.username or p.password:
            return ''
        if any(ord(ch) < 32 or ord(ch) == 127 for ch in value):
            return ''
        return value
    except ValueError:
        return ''


def require_string(data, key):
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{key}: non-empty string required')
    return value.strip()


def render(data):
    if not isinstance(data, dict):
        raise ValueError('JSON root must be object')
    kind = require_string(data, 'kind')
    if kind not in KIND_NAMES:
        raise ValueError('kind must be secretary / project / routine')
    title = require_string(data, 'title')
    snapshot_date = require_string(data, 'snapshot_date')
    checked = require_string(data, 'source_checked_at')
    source_label = require_string(data, 'source_label')
    source_url = approved_href(data.get('source_url', ''))
    summary = str(data.get('summary') or '')
    handoff = str(data.get('handoff') or '')
    visibility = data.get('visibility', 'private')
    if visibility not in ('private', 'public'):
        raise ValueError('visibility must be private or public')
    items = data.get('items', [])
    if not isinstance(items, list) or len(items) > 1000:
        raise ValueError('items must be list with at most 1000 entries')

    cards = []
    for n, item in enumerate(items):
        if not isinstance(item, dict):
            raise ValueError(f'items[{n}] must be object')
        name = str(item.get('title') or '').strip()
        if not name:
            raise ValueError(f'items[{n}].title required')
        priority = str(item.get('priority') or 'OTHER').upper()
        if priority not in PRIORITIES:
            priority = 'OTHER'
        url = approved_href(item.get('source_url', ''))
        period = str(item.get('period') or item.get('due') or '').strip()
        period_html = f'<div><dt>対象期間／期限</dt><dd>{h(period)}</dd></div>' if period else ''
        link = (f'<a class="source" href="{h(url)}" target="_blank" rel="noopener noreferrer">元記録へ</a>' if url else '')
        cards.append(f'''<article class="item" data-priority="{priority}">
          <div class="item-top"><span class="priority">{priority}</span><span class="id">{h(item.get('id', ''))}</span></div>
          <h3>{h(name)}</h3><dl>{period_html}
          <div><dt>状態</dt><dd>{h(item.get('status', '未確認'))}</dd></div>
          <div><dt>担当</dt><dd>{h(item.get('owner', '未確認'))}</dd></div>
          <div><dt>次の一手</dt><dd>{h(item.get('next_action', '未確認'))}</dd></div>
          <div><dt>根拠</dt><dd>{h(item.get('evidence', '未確認'))}</dd></div>
          </dl>{link}</article>''')
    source_link = (f'<a href="{h(source_url)}" target="_blank" rel="noopener noreferrer">{h(source_label)}</a>'
                   if source_url else h(source_label) + '（URL未提供）')
    report_text = '\n'.join([
        f'{title} / {KIND_NAMES[kind]} / VIEW SNAPSHOT',
        f'対象日: {snapshot_date}', f'出典確認時刻: {checked}',
        f'正本: {source_label} {source_url}', f'要約: {summary}',
    ] + [f"{i.get('id','')} | {i.get('title','')} | {i.get('status','未確認')} | {i.get('next_action','未確認')}"
         for i in items])
    # Textareas store escaped text; no source content is interpolated into JavaScript.
    css = '''
:root{--adnc-ink:#192d43;--adnc-navy:#11243e;--adnc-teal:#087f7b;--adnc-link:#0b6d92;--adnc-bg:#f6fafd;--adnc-line:#d2e5e9;font-family:"Noto Sans JP",system-ui,-apple-system,sans-serif;color:var(--adnc-ink);background:var(--adnc-bg)}
*{box-sizing:border-box}body{margin:0}header{background:var(--adnc-navy);color:#fff;padding:25px 5vw}main{max-width:1150px;margin:auto;padding:20px}
h1{font-size:clamp(1.35rem,3.3vw,2.3rem);margin:9px 0}h2{font-size:1.24rem}h3{font-size:1.05rem;margin:9px 0 15px}
.eyebrow{font-size:.85rem;color:#8fe4d8;letter-spacing:.04em}.status{font-weight:700}.panel{background:#fff;border:1px solid #d2e5e9;border-radius:16px;padding:18px;margin:15px 0;box-shadow:0 3px 14px #1b36400b}
.summary{white-space:pre-wrap;line-height:1.7}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:12px}
.item{border:1px solid #cfe5ea;background:#fff;border-radius:13px;padding:16px}.item-top{display:flex;justify-content:space-between;gap:7px;color:#53687c;font-size:.8rem}
.priority{background:#e6f7f3;color:#155c57;border-radius:8px;padding:2px 8px;font-weight:700}.id{overflow-wrap:anywhere}dl{margin:0}dl div{margin:7px 0;line-height:1.5}dt{color:#53687c;font-size:.78rem}dd{margin:0;overflow-wrap:anywhere}
a{color:#0b6d92;overflow-wrap:anywhere}.source{display:inline-block;margin-top:8px}button{cursor:pointer;border:1px solid #b6d8dc;border-radius:11px;background:#fff;color:#11243e;padding:9px 13px;font-size:.94rem;margin:4px}
button[aria-pressed=true]{background:var(--adnc-teal);color:#fff}button:focus-visible,a:focus-visible{outline:3px solid var(--adnc-teal);outline-offset:2px}
fieldset{border:0;padding:0;margin:0}legend{font-weight:700;margin:7px 0}.muted{color:#53687c;font-size:.9rem}.hide{display:none!important}
pre{white-space:pre-wrap;overflow-wrap:anywhere}textarea{width:100%;min-height:130px}footer{padding:18px 5vw;color:#53687c}
@media(max-width:440px){header{padding:17px 5vw}main{padding:10px}.panel{padding:13px}.grid{grid-template-columns:1fr}}
'''
    js = r'''
(function(){'use strict';
 const cards=Array.from(document.querySelectorAll('.item'));
 const count=document.getElementById('counter');
 document.querySelectorAll('[data-filter]').forEach(function(button){button.addEventListener('click',function(){
   const level=button.dataset.filter;let visible=0;
   cards.forEach(function(card){const show=level==='all'||card.dataset.priority===level;card.classList.toggle('hide',!show);if(show)visible++;});
   document.querySelectorAll('[data-filter]').forEach(function(b){b.setAttribute('aria-pressed',String(b===button));});
   count.textContent=visible+'件を表示';
 });});
 document.querySelectorAll('[data-copy]').forEach(function(button){button.addEventListener('click',async function(){
   const textarea=document.getElementById(button.dataset.copy),note=document.getElementById('copy-result');
   if(!textarea)return;const data=textarea.value;
   try{if(!navigator.clipboard||!navigator.clipboard.writeText)throw Error('unavailable');await navigator.clipboard.writeText(data);
     note.textContent='全文をコピーしました（送信・登録はしていません）。';return;
   }catch(_e){}
   textarea.classList.remove('hide');textarea.focus();textarea.select();
   try{if(document.execCommand&&document.execCommand('copy')){note.textContent='全文をコピーしました（互換方式）。';return;}}catch(_e){}
   note.textContent='自動コピー不可。下の選択済み全文を手動でコピーしてください。';
 });});
})();'''
    filters = ''.join(f'<button type="button" data-filter="{level}" aria-pressed="{str(level=="all").lower()}">{level if level != "all" else "全件"}</button>' for level in ('all','P0','P1','P2','OTHER'))
    return f'''<!doctype html><html lang="ja" data-report-kind="{kind}" data-view-kind="snapshot" data-adnc-design="visual-docs-v0.1"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="referrer" content="no-referrer">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; connect-src 'none'; img-src 'none'; object-src 'none'; form-action 'none'; base-uri 'none'">
<title>{h(title)}</title><style>{css}</style></head><body>
<header><div class="eyebrow">AD&amp;C · {h(KIND_NAMES[kind])} · VIEW / SNAPSHOT</div><h1>{h(title)}</h1>
<p>{h(snapshot_date)} | 元記録確認：{h(checked)} | {h(visibility).upper()}</p></header>
<main><section class="panel"><h2>今回の要点</h2><div class="summary">{h(summary)}</div>
<p class="muted">固定時点の閲覧用です。正本の更新・定時実行・通知・承認は行いません。</p></section>
<section class="panel"><h2>案件・実行回</h2><fieldset><legend>優先度で絞り込む</legend>{filters}</fieldset>
<p id="counter" aria-live="polite">{len(cards)}件を表示</p><div class="grid">{''.join(cards)}</div></section>
<section class="panel"><h2>元の記録</h2><p>{source_link}</p><p class="muted">閲覧権限がある場合のみ開けます。ここから勝手に更新しません。</p></section>
<section class="panel"><h2>引継ぎ・全文コピー</h2>
<button type="button" data-copy="handoff">引継ぎ文を全文コピー</button><button type="button" data-copy="report">報告全文をコピー</button>
<p id="copy-result" aria-live="polite" class="muted"></p>
<details><summary>引継ぎ文の全文を確認</summary><pre>{h(handoff)}</pre></details>
<details><summary>報告の全文を確認</summary><pre>{h(report_text)}</pre></details>
<label for="handoff" class="muted">引継ぎ文（コピー不可時にも選択可能）</label><textarea class="hide" id="handoff" readonly>{h(handoff)}</textarea>
<label for="report" class="muted">報告全文（コピー不可時にも選択可能）</label><textarea class="hide" id="report" readonly>{h(report_text)}</textarea></section></main>
<footer>AD&amp;C / READ-ONLY VIEW · {h(checked)}</footer><script>{js}</script></body></html>'''


def main():
    p = argparse.ArgumentParser(description='Render a static, offline AD&C report without network calls')
    p.add_argument('input', type=Path, help='UTF-8 JSON prepared from authorized existing records')
    p.add_argument('output', type=Path, help='HTML output path; private location by default')
    args = p.parse_args()
    data = json.loads(args.input.read_text(encoding='utf-8'))
    result = render(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding='utf-8')
    print(f'OK: {args.output} ({len(result.encode("utf-8"))} bytes)')


if __name__ == '__main__':
    main()