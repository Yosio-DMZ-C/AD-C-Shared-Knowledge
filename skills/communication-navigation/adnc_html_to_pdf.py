#!/usr/bin/env python3
"""AD&C: render a one-column, mobile-readable dashboard PDF from a local HTML snapshot.

This optional deterministic tool does NOT upload data. Show only the resulting PDF
link to the human; HTML remains an intermediate. Ordinary chat / secretary Q&A
continues independently. No new KB or task is created.

Run:
  python adnc_html_to_pdf.py INPUT.html --output /tmp/ADNC_Dashboard.pdf
Requirements: pip install playwright  (Chromium must be installed / discoverable)
Optional checks: pip install pymupdf
Optional logo: --logo-file /path/to/verified_official_logo.png
Do not claim a live link exists until the calling AI actually exports the PDF.
"""
from __future__ import annotations

import argparse
import base64
import json
import shutil
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

OFFICIAL_LOGO_URL = (
    "https://campsite7.jp/wp-content/uploads/2026/11/"
    "adnc-logo-compass-wordmark-20261016-684f1714.png"
)

PRINT_CSS = r"""
@page { size: A4 portrait; margin: 12mm 13mm; }
html, body { width: auto !important; height: auto !important; overflow: visible !important; }
body { background: white !important; font-size: 14px !important; line-height: 1.65 !important; }
.shell, .content, main { width: auto !important; max-width: none !important; }
.columns, .grid, .metrics, .stats, .links, .hero-grid, .stack,
.btnrow, .row, .event, .foot, .topbar .shell, .hero-meta {
  display: block !important; grid-template-columns: none !important;
  column-count: 1 !important; columns: auto !important;
}
.columns > *, .grid > *, .metrics > *, .stats > *, .links > *,
.metric, .stat, .panel, .card, .event, .row-info {
  width: 100% !important; max-width: 100% !important;
  margin-bottom: 11px !important; float: none !important; position: static !important;
}
.panel, .card, .metric, .stat { box-shadow: none !important; }
.panel, .card { break-inside: auto !important; page-break-inside: auto !important; }
h1, h2, h3, summary { break-after: avoid !important; }
p, li { orphans: 2; widows: 2; }
.hero-orb { display: none !important; }
button, .copy-status, .copy-fallback, .btnrow, [data-copy] { display: none !important; }
details .inner { display: block !important; }
pre, code { white-space: pre-wrap !important; overflow-wrap: anywhere !important;
  word-break: break-word !important; }
a { overflow-wrap: anywhere !important; }
.adnc-official-logo { display: block; width: auto; height: auto;
  max-width: 105px; max-height: 40px; object-fit: contain; margin: 4px 0 6px; }
"""

def optional_logo_bytes(path: Path | None, try_web: bool) -> tuple[bytes | None, str]:
    if path:
        try:
            data = path.read_bytes()
            if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) <= 2_000_000:
                return data, "local"
            return None, "invalid_local_png"
        except OSError:
            return None, "unreadable_local"
    if not try_web:
        return None, "skipped"
    try:
        req = urllib.request.Request(
            OFFICIAL_LOGO_URL, headers={"User-Agent": "ADNC-Dashboard/1.0"}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            if urllib.parse.urlparse(response.geturl()).hostname != "campsite7.jp":
                return None, "unexpected_logo_host"
            data = response.read(2_000_001)
        if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) <= 2_000_000:
            return data, "official_web"
        return None, "invalid_remote_png"
    except (OSError, urllib.error.URLError, TimeoutError):
        return None, "unavailable_web_logo"

def convert(html: Path, output: Path, logo: bytes | None) -> list[str]:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise RuntimeError("Playwright unavailable") from exc
    output.parent.mkdir(parents=True, exist_ok=True)
    blocked: list[str] = []
    with sync_playwright() as pw:
        launch = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
        chromium = shutil.which("chromium") or shutil.which("google-chrome")
        if chromium:
            launch["executable_path"] = chromium
        browser = pw.chromium.launch(**launch)
        try:
            page = browser.new_page(viewport={"width": 390, "height": 844})
            def local_only(route):
                uri = route.request.url
                if uri.startswith(("https:", "http:")):
                    blocked.append(uri)
                    route.abort()
                else:
                    route.continue_()
            page.route("**/*", local_only)
            page.set_content(html.read_text(encoding="utf-8"),
                             wait_until="load", timeout=20000)
            page.evaluate("document.querySelectorAll('details').forEach(el => el.open = true)")
            if logo:
                data = base64.b64encode(logo).decode("ascii")
                page.evaluate("""b64 => {
                  const img = document.createElement('img');
                  img.alt = 'AD&C 公式ロゴ'; img.className = 'adnc-official-logo';
                  img.src = 'data:image/png;base64,' + b64;
                  const host = document.querySelector('.hero .shell') ||
                    document.querySelector('header .shell') ||
                    document.querySelector('header') || document.body;
                  host.prepend(img);
                }""", data)
            page.add_style_tag(content=PRINT_CSS)
            page.emulate_media(media="print")
            page.pdf(path=str(output), format="A4", print_background=True,
                     prefer_css_page_size=True, display_header_footer=False)
        finally:
            browser.close()
    if not output.is_file() or output.stat().st_size < 1000:
        raise RuntimeError("PDF output not generated")
    return blocked

def main() -> int:
    cli = argparse.ArgumentParser(description="AD&C dashboard HTML -> temporary PDF")
    cli.add_argument("html", type=Path, help="locally generated single-file HTML")
    cli.add_argument("--output", type=Path, help="temporary PDF file path")
    cli.add_argument("--logo-file", type=Path, help="optional verified official PNG")
    cli.add_argument("--no-web-logo", action="store_true")
    args = cli.parse_args()
    if not args.html.is_file() or args.html.suffix.lower() != ".html":
        print(json.dumps({"status": "FAIL", "reason": "HTML input not found"}))
        return 2
    output = args.output or Path(tempfile.mkdtemp(prefix="adnc_pdf_")) / (
        args.html.stem + ".pdf"
    )
    if output.suffix.lower() != ".pdf":
        print(json.dumps({"status": "FAIL", "reason": "Output must end in .pdf"}))
        return 2
    logo, logo_state = optional_logo_bytes(args.logo_file, not args.no_web_logo)
    try:
        blocked = convert(args.html, output, logo)
        result = {"status": "PASS", "pdf": str(output),
                  "logo": logo_state, "blocked_external_requests": len(blocked),
                  "bytes": output.stat().st_size}
        try:
            import fitz
            with fitz.open(output) as doc:
                result.update(pages=len(doc),
                              selectable_text=any(p.get_text().strip() for p in doc),
                              source_links=sum(len(p.get_links()) for p in doc))
        except ImportError:
            result["pdf_validation"] = "NOT_RUN (PyMuPDF absent)"
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc),
                          "fallback": "text report and one-question chat continue"},
                         ensure_ascii=False))
        return 1

if __name__ == "__main__":
    sys.exit(main())
