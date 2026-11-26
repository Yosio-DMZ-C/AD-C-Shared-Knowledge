"""Render an AD&C leader snapshot PDF with ReportLab's built-in Japanese CID font."""
from __future__ import annotations

from html import escape
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


def render(data: dict, output: Path) -> dict:
    """Write a Japanese PDF from normalized dashboard data; preserve HTTPS source links."""
    font = "HeiseiKakuGo-W5"
    if font not in pdfmetrics.getRegisteredFontNames():
        pdfmetrics.registerFont(UnicodeCIDFont(font))
    base = getSampleStyleSheet()
    title = ParagraphStyle("ADNCTitle", parent=base["Title"], fontName=font,
                           fontSize=18, leading=24, textColor=colors.HexColor("#11243e"), alignment=TA_LEFT)
    h2 = ParagraphStyle("ADNCH2", parent=base["Heading2"], fontName=font,
                        fontSize=12, leading=17, textColor=colors.HexColor("#087f7b"), spaceBefore=8, spaceAfter=5)
    body = ParagraphStyle("ADNCBody", parent=base["BodyText"], fontName=font,
                          fontSize=9, leading=14, textColor=colors.HexColor("#192d43"), wordWrap="CJK")
    small = ParagraphStyle("ADNCSmall", parent=body, fontSize=8, leading=11, textColor=colors.HexColor("#53687c"))
    card_head = ParagraphStyle("ADNCCardHead", parent=h2, fontSize=11, leading=15, spaceBefore=0, spaceAfter=2)

    def p(value, style=body):
        return Paragraph(escape("" if value is None else str(value)).replace("\n", "<br/>"), style)

    story = [p(f'{data["meta"]["project_or_work"]}｜リーダーダッシュボード', title),
             p(f'{data["meta"]["organization"]}　責任: {data["meta"]["responsibility"]}', small),
             p(f'管理範囲: {data["meta"]["scope"]}　取得時点: {data["meta"]["retrieved_at"]}', small),
             Spacer(1, 4*mm), p("今回の要点", h2), p(data.get("summary", "")),
             p("カテゴリは独立分母です。縦合計・進捗率の推測はありません。", small),
             p(f'次の1操作: {data.get("next_action", "未確認")}', body), Spacer(1, 3*mm)]
    for category in data.get("categories", []):
        ach = "　".join(f'{k}={"未集計" if v is None else str(v)+"件"}' for k, v in category.get("achievement", {}).items())
        denom = category.get("denominator")
        count = "未集計" if denom is None else f"{denom}件"
        header = p(f'{category.get("label", category.get("id", ""))}　｜　未解決分母 {count}', card_head)
        details = [p(f'実績: {ach}', small)]
        states = category.get("states") or {}
        if states:
            details.append(p("状態内訳: " + "　".join(f"{k.upper()}={v}件" for k, v in states.items()), small))
        category_block = [header, *details]
        for item in category.get("items", []):
            fields = [p(str(item.get("title", "未確認")), card_head)]
            fields.append(p(f'ID: {item.get("id", "")}　状態: {item.get("status", "未確認")}　担当: {item.get("owner", "未確認")}', small))
            fields.append(p(f'次の一手: {item.get("next_action", "未確認")}', body))
            fields.append(p(f'根拠: {item.get("evidence", "未確認")}', small))
            url = item.get("source_url") or ""
            if isinstance(url, str) and url.startswith("https://"):
                safe = escape(url, quote=True)
                fields.append(Paragraph(f'<link href="{safe}" color="#0b6d92">元記録へ</link>', small))
            category_block.append(Spacer(1, 2*mm))
            category_block.append(KeepTogether(fields))
        story.append(KeepTogether(category_block[:2]))
        story.extend(category_block[2:])
        story.append(Spacer(1, 4*mm))
    src = data.get("source", {})
    if src:
        story += [p("元の記録", h2)]
        for label, url in src.items():
            if isinstance(url, str) and url.startswith("https://"):
                story.append(Paragraph(f'{escape(str(label))}: <link href="{escape(url, quote=True)}" color="#0b6d92">{escape(url)}</link>', small))
            else:
                story.append(p(str(label), small))

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, rightMargin=17*mm, leftMargin=17*mm,
                            topMargin=15*mm, bottomMargin=15*mm, title="AD&C Leader Dashboard")
    doc.build(story)
    return {"pdf": str(output), "bytes": output.stat().st_size}
