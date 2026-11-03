# AD&C step-list generation pilot — leader Playbook only

Status: **pilot / not production-approved**. Scope: `docs/templates/LEADER_WORKSHEET.md` only. This proposal does **not** authorize any other Playbook changes or automatic execution.

## Three separated responsibilities

1. **Human-readable Playbook:** purpose, authorization, stop conditions, recovery, and judgment stay in human-editable prose.
2. **Bounded list generator:** the inspected `python adnc-generated-steps` block renders numbered steps **only** inside exactly one `<!-- ADNC:AUTO:BEGIN -->` / `<!-- ADNC:AUTO:END -->` pair. This stage neither performs steps nor changes authorization or status.
3. **Executor and verifier:** an authorized AI/operator reads the prose and list, checks current permissions, SHA/conflicts and backup, performs actions with available tools, and separately verifies real artifacts/readback. Generation PASS is not execution PASS.

## Strict exclusion from batch rollout

**Never bulk-apply to creative Playbooks**, including video production, thumbnail/image creation, animation, narration, editing, or any Playbook involving subjective composition or aesthetics. They require a separate specialist design review and independent creative acceptance test. The generator must not replace prompts, creative choices, asset handling, character/logo composition, editorial decisions, or final visual QA.

Other Playbooks are also **not automatically in scope**. Each must be explicitly inventoried and approved for its own pilot; no mass rewrite, migration, or automatic activation.

## Leader pilot acceptance gates

- Pin main commit and blob SHA, preserve original raw bytes and recovery copy.
- Inspect the exact embedded Python before isolated execution. Never execute arbitrary Markdown code from an untrusted source.
- Require one correctly ordered AUTO marker pair and one exact named Python fence. Reject malformed, duplicated, reversed, or missing markers.
- Require an exact expected input SHA before any write; reject stale SHA or conflict.
- Replace only the marked AUTO content; preserve all bytes outside it, including line endings and UTF-8.
- Run twice and require byte-for-byte idempotence, valid UTF-8, and no duplicated sections.
- Verify immutable backup and byte-exact restoration.
- Execute the generated steps **separately**; record operation and outcome PASS/FAIL/NOT_RUN independently.
- Production writes require a separately approved runner, write interface, original-file readback and any dependent registry/link checks. A local test alone is not operational PASS.

## Pilot evidence / current limit

The isolated independent verification identified that `render_steps()` renders a string but does not itself write Markdown, enforce SHA, or back up files. A separate tested adapter is required. The locally exercised list check does not execute any listed action. Therefore this pilot stays OPEN until a reviewed runner and actual authorized end-to-end readback pass.

**Decision gate:** adopt this separation for the leader pilot only. No blanket rollout. Creative work remains excluded even after a leader pilot PASS.
