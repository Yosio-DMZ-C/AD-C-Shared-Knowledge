#!/usr/bin/env python3
"""AD&C secretary: deterministic JST dates and dialogue flags only.
No network, account reads, writes, task creation, or automatic approvals.
Use authorized existing records as optional JSON input; do not upload private inputs.
"""
import argparse
import json
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

JST = ZoneInfo('Asia/Tokyo')


def iso_boundary(day):
    return day.isoformat() + 'T00:00:00+09:00'


def age_days(today, value):
    if not value:
        return None
    try:
        delta = (today - date.fromisoformat(value)).days
        return delta if delta >= 0 else None
    except (TypeError, ValueError):
        return None


def compute(data, today=None):
    if not isinstance(data, dict):
        raise ValueError('State must be a JSON object')
    today = today or datetime.now(JST).date()
    if isinstance(today, str):
        today = date.fromisoformat(today)
    month_key = f'{today:%Y-%m}-H{1 if today.day <= 15 else 2}'
    completed_age = age_days(today, data.get('monthly_completed_on'))
    prompted_age = age_days(today, data.get('monthly_prompted_on'))
    already = data.get('monthly_already_answered')
    requested = data.get('user_requested_monthly') is True
    if requested:
        monthly = 'YES_USER_REQUEST'
    elif already is True:
        monthly = 'NO_ALREADY_ANSWERED'
    elif completed_age is None or already is None:
        monthly = 'UNKNOWN'
    elif data.get('monthly_prompted_on') and prompted_age is None:
        monthly = 'UNKNOWN'
    else:
        monthly = 'YES' if completed_age >= 40 and (prompted_age is None or prompted_age >= 30) else 'NO'
    n = data.get('unresolved_for_human')
    question = 'YES' if isinstance(n, int) and not isinstance(n, bool) and n > 0 else ('NO' if n == 0 and not isinstance(n, bool) else 'UNKNOWN')
    statuses = {'DONE': 0, 'DONE_WITH_ISSUES': 0, 'OPEN': 0, 'UNKNOWN': 0}
    items = data.get('items') or []
    if not isinstance(items, list):
        raise ValueError('items must be a list')
    for item in items:
        if not isinstance(item, dict):
            raise ValueError('items entries must be objects')
        status = str(item.get('status', 'UNKNOWN')).upper()
        statuses[status if status in statuses else 'UNKNOWN'] += 1
    return {
        'jst_date': today.isoformat(),
        'calendar_primary_today': {'time_min': iso_boundary(today), 'time_max': iso_boundary(today + timedelta(days=1))},
        'calendar_primary_next7d': {'time_min': iso_boundary(today), 'time_max': iso_boundary(today + timedelta(days=7))},
        'half_month_key': month_key,
        'monthly_prompt': monthly,
        'one_question_entry': question,
        'status_counts': statuses,
        'independent_jobs': ['save_daily_log', 'generate_pdf'],
        'note': 'Calendar/Gmail/Drive reads, real writes, PDF creation and UI clicks are NOT_RUN by this helper.'
    }


def main():
    cli = argparse.ArgumentParser(description='Calculate AD&C secretary deterministic flags without service access')
    cli.add_argument('--state', type=Path, help='optional private JSON with verified case state')
    cli.add_argument('--date', help='JST date YYYY-MM-DD; default current JST date')
    cli.add_argument('--output', type=Path, help='optional JSON output; else stdout')
    args = cli.parse_args()
    data = json.loads(args.state.read_text(encoding='utf-8')) if args.state else {}
    result = compute(data, args.date)
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.output:
        args.output.write_text(rendered, encoding='utf-8')
    else:
        print(rendered, end='')


if __name__ == '__main__':
    main()
