#!/usr/bin/env bash
# Static contract gate for the public OneShot Draft; no execution of payload.
set -euo pipefail

usage() {
  echo 'Usage: check_oneshot_contract.sh KIT.zip SCRIPT.sh [REPORT.txt]' >&2
  exit 64
}
fail() { echo "FAIL: $*" >&2; exit 1; }

[ "$#" -ge 2 ] && [ "$#" -le 3 ] || usage
zip_file=$1
script_name=$2
report=${3:-}
[ -f "$zip_file" ] || fail 'ZIP not found'
case "$script_name" in ''|/*|*'../'*) fail 'Pass the exact relative script path inside ZIP' ;; esac
case "$script_name" in *'*'*|*'?'*|*'['*|*']'*) fail 'ZIP script name must not contain wildcard characters' ;; esac
command -v unzip >/dev/null 2>&1 || fail 'unzip is unavailable'
command -v bash >/dev/null 2>&1 || fail 'bash is unavailable'
unzip -tqq "$zip_file" >/dev/null || fail 'ZIP integrity check failed'
member_count=$(unzip -Z -1 "$zip_file" | awk -v target="$script_name" '$0==target {n++} END {print n+0}')
[ "$member_count" -eq 1 ] || fail 'Expected exactly one matching ZIP script member'
unzip -p "$zip_file" "$script_name" | bash -n || fail 'Shell syntax failed'

if [ -n "$report" ]; then
  [ -f "$report" ] || fail 'REPORT not found'
  awk '
    BEGIN {n=split("TASK MODE TARGET BACKUP RESULT FUNCTION_TEST REPORT NEXT", keys, " "); bad=0}
    {
      if (NR>n || index($0,keys[NR] ":")!=1) {print "FAIL: report key/order at line " NR > "/dev/stderr";bad=1;next}
      value=substr($0,length(keys[NR])+2); sub(/^[[:space:]]*/,"",value)
      if (value=="") {print "FAIL: empty value at line " NR > "/dev/stderr";bad=1}
      if (NR==2 && value !~ /^(audit|apply|rollback)$/) {print "FAIL: invalid MODE" > "/dev/stderr";bad=1}
      if (NR==5 && value !~ /^(READ_ONLY_PASS|PATCH_APPLIED|ALREADY_APPLIED|ROLLED_BACK|FAIL|NOT_RUN)$/) {print "FAIL: invalid RESULT" > "/dev/stderr";bad=1}
      if (NR==6 && value !~ /^(NOT_TESTED|PASS|FAIL)$/) {print "FAIL: invalid FUNCTION_TEST" > "/dev/stderr";bad=1}
    }
    END {if (NR!=n) {print "FAIL: expected 8 report lines" > "/dev/stderr";bad=1};exit bad}
  ' "$report" || fail 'REPORT format failed'
fi

echo 'PASS: ZIP integrity, unique entry name, bash syntax; report format checked only if supplied.'
