# Leader worksheet v0.1

Use this worksheet during the work, then reuse it as the final report. This is a format, not a decision procedure. Refer to the existing registry and operating rules for authoritative facts and approvals.

**Execution model (2026-10-29 β):** Team members complete their authorized reversible changes through canonical writes, reference/Git integration and readback; the leader audits across changes and repairs scoped inconsistencies. Keep the existing three daily scheduled reviews and two-pass audit; this worksheet does not reschedule or weaken them. Audit significant dependencies and actual restorability, not just reported completion. Avoid new trackers and duplicate approval prompts.

1. New changes: record only new facts, or 'no new changes'.
2. Reconciliation: note sources checked, discrepancies, and unverified claims.
3. Implementation: record actual writes, commits, readback, and PASS / FAIL / NOT_RUN.
4. Recovery: identify prior version and whether rollback was actually tested.
5. Next action: one priority and, if needed, one approval question.

Keep routine reports brief. Mark irrelevant checks N/A with a reason. Never report a draft or unverified change as DONE.

## Data-write propagation gate for all agents (2026-11-02; proposed)

This is a **cross-agent acceptance check**, not a second private-KB playbook. Before the secretary, leader, scheduled task, or delegated AI writes into an existing KB, fetch its CURRENT entry → registry/INDEX → canonical write/update procedure **in full**, from within the authorized environment. Do not substitute this public worksheet for private KB write instructions. Reading a link or an old summary is not receipt of the current procedure.

Treat a write as one dependency chain: determine authorized scope and exact existing ID/current raw SHA → verify a byte-matching pre-write recovery source and conflicts → apply the minimum same-ID write → independently re-fetch raw bytes → recompute SHA and update existing registry entries and affected INDEX/context/reverse links → re-fetch all affected destinations. If a dependency remains stale or unknown, record the original parent as OPEN with observed failure, cause investigation and concrete unblock step. A successful Drive upload alone is never registry-sync PASS. Do not mask unresolved causes with an invented explanation.

Keep human-readable purpose/decisions/stop rules in the existing natural-language procedure; use tested adapters or Python only for bounded mechanical checks. Respect separate permissions and public-main approval. Never copy private registry contents, Drive IDs/URLs, client data, or credentials to this public GitHub repo. Passing the rule to a task prompt is not proof a different chat or AI actually complied; independently exercised receipt and behavior are separate gates.

## Implementation-first policy
When the user requests implementation, carry the approved, reversible work through the canonical source, necessary references, Git, and readback. Do not stop at a proposal, worksheet, or PR and call it done. Avoid repeated approval questions for the same authorized scope. Stop and ask only for a genuinely new approval boundary, an irreversible action, a public disclosure, or a blocked operation. Record remaining work in the existing tracker rather than creating duplicate open items.

## Exit gate (before reporting)
Immediately before the final response, compare the user's requested outcome with actual canonical writes, required Git state, reference updates, and readback evidence. If an approved, safe step remains, perform it rather than stopping to propose it. If blocked by a genuine approval or safety boundary, mark the exact step NOT_RUN and report the reason; do not mark the task DONE.

### β is a release stage, not a completion status (2026-10-29)

At the exit gate, **never use “β”, “experimental”, “research”, “PR prepared”, or “next phase” to close or downgrade an originally requested implementation**. Check three independent facts only where they are part of the original acceptance criteria: **(1) implementation** = required canonical source, Git/main (if required), dependent references/settings, and readback actually match; **(2) operation** = requested working path or independent recipient actually ran; **(3) effect** = the requested outcome or comparative evidence was actually measured. Mark each `PASS / FAIL / NOT_RUN / N/A (reason)`, and keep the *original parent task OPEN* for missing required parts. A committed **instruction** is implementation PASS for that instruction, **not** proof that other AI agents obeyed it. If only the effect study remains, report “rule implemented; effect NOT_RUN” without relabeling the implementation as unfinished or inventing an open-ended new project. Fix an authorized safe missing step now; stop only at a real blocker. In routine no-change reviews, one concise status line suffices; do not create another ledger or audit pass.

## No 'separate process' escape
A requested outcome remains one tracked item across its substeps. Never close or defer an unfinished substep merely by labeling it 'separate process', 'next time', 'handoff', or 'PR prepared'. Before reporting, enumerate every remaining substep and attempt each authorized, safe action now. For each unexecuted substep, name the exact blocker (specific missing approval, permission, unavailable tool, conflict, or failed recovery check), evidence, and the single action that would unblock it. A different workflow or repository is not itself a blocker. Keep the parent item OPEN until the requested canonical end state and readback are verified. Do not treat a general implementation request as approval for public-main merges or other restricted actions.

## Human-time principle (experimental)

**Short rationale cue at a decision boundary (β, not evidence of effectiveness):** “Human time is limited; repeating approvals and deferring already authorized, reversible work create costs. After verifying actual authorization, pre-change state, conflicts and recovery path, finish safe steps through readback. Pause only for a new approval or unsafe/unrecoverable condition.” The cue never authorizes a write and never overrides a required approval or safety stop. Evaluate on existing T005 scenarios: A = safety baseline, B = exit check only, C = cue plus exit check; compare completion, extra questions, delays and safety violations. Do not add a third routine audit loop or a new checklist. Report all behavioral effects as NOT_RUN until observed.

Human time is finite and nonrenewable: five minutes now matter as much as five minutes near the end of life. Unnecessary repeated approval requests, forgotten unfinished work, and vague deferrals waste that time. AD&C already defines safeguards for backups, recovery, conflict checks, and authorization; verify those safeguards rather than assuming either safety or danger. Once they pass, complete authorized reversible work without asking again. Never use this principle to override an actual safety boundary. If several genuine decisions remain, present only the highest-priority actionable decision, then continue after it is resolved. Record the others in the existing tracker, not a new list. Treat this wording as an interface hypothesis, not a validated behavioral effect.

## Pending-item provenance
For every unfinished action, report: `NOT_RUN (origin: original parent request; action: exact remaining step; blocker: verified reason or unverified; unblock: next concrete action)`. Keep the parent OPEN until its intended end state is verified. A different workflow or repository is not a blocker. Distinguish not attempted from failed execution; never ask for blanket approval.

## Unfinished work and retry
Every action not performed must be labeled `未実施（元工程：...／理由：...）`. Keep its parent task OPEN. A different workflow is not a reason to omit this label. For a transient tool failure, retry once after checking whether the first attempt succeeded, to avoid duplicate writes. Do not retry authorization denials, irreversible actions, or safety blocks automatically. Record the outcome of both attempts.

## Entry-first creation and acceptance
Before creating or substantially revising a playbook or worksheet, check existing shared/personal KB procedures and Skills for equivalent purpose; distinguish Active, Draft, superseded, and withdrawn. Define a natural-language request that should lead to the procedure, its directly fetchable canonical source, version and applicability. Treat `request → discover → fetch → execute in specified order → inspect required output → present useful result` as one deliverable. A README link alone is not automatic discovery. Map evidence to existing Q1 (entry and document), Q2 (independent cold-start interpretation), Q3 (actual sequence and safety gates), and Q4 (user-facing result); untested stages remain `未実施（元工程：...／理由：...）`. Avoid creating another registry or gate. Preserve private identifiers outside public KB.

## Markdown-embedded Python pilot (candidate; not adopted in main)

Human-editable purpose, authorization, stop conditions, and recovery rules remain authoritative prose. A trusted runner MAY extract the fenced block labeled `python adnc-generated-steps`, execute it only in an isolated no-network test environment, and replace only text between the two AUTO markers. Never execute arbitrary downloaded Markdown code or silently overwrite human prose. For production use, require approved runtime, exact pre-write SHA, conflict check, backup and restore test, and readback. Thumbnail/image composition remains excluded pending separate specialist review.

<!-- ADNC:AUTO:BEGIN -->
1. Read current canonical source and record its revision.
2. Check authorization, conflict and recovery evidence.
3. Execute only authorized reversible actions; read back and report.
<!-- ADNC:AUTO:END -->

```python adnc-generated-steps
STEPS = [
    "Read current canonical source and record its revision.",
    "Check authorization, conflict and recovery evidence.",
    "Execute only authorized reversible actions; read back and report.",
]
def render_steps():
    return "\\n".join(f"{i}. {step}" for i, step in enumerate(STEPS, 1))
```

Pilot acceptance: preserve all text outside AUTO markers byte-for-byte, compare expected SHA before write, verify idempotence, and restore from a verified backup. A successful isolated pilot does not prove a Drive write, an AI cold start, or production execution.


## Completion-through-repair rule (2026-11-02, user-approved)

When asked to **修正・検証する**, do not stop at inspecting, proposing, drafting, opening a PR, or recording NOT_RUN. Attempt every remaining in-scope, authorized, safe step **in this execution**: resolve the correct canonical document and registry entry, obtain pre-edit bytes/ID/version and recovery copy, diagnose write-interface and conflict failures, modify the original canonical file (same ID when required), update dependent links/indexes and required Git/main, then re-fetch each destination and compare intended content. A failed first attempt is a reason for targeted diagnosis and one safe retry after checking whether the first write took effect, not an automatic end of work. Seek an equivalent supported write mechanism when the initially selected connector cannot complete the operation; avoid duplicate or replacement files presented as original changes.

**Exit decision is based on the user's outcome, not on the amount of work performed.** Only report completed when every required canonical and downstream acceptance check is PASS. A file being fetched, a draft being made, or a blocker being described is not the requested completion. If—and only if—a concrete permission, safety, irreversibility, exhausted technical route, or verified external-dependency boundary actually prevents completion, record the exact parent/step, observed cause, attempted recovery, and specific unblock action in the existing tracker, plus FAIL/NOT_RUN; do not conceal, downgrade, or forget the unfinished parent. Routine Git changes/merge are within the user-approved scope when needed for the intended result, but this does not authorize leaking private KB into public GitHub, deletion, privilege changes or unreviewed production effects.

## Scheduled leader execution contract (2026-11-02)

This section is the external operational contract for the existing three-times-daily leader automation; the worksheet above remains its report template. Follow private START_HERE → registry → current leader Playbook → 80_reviews, Context, BUILD_PLAN and OPERATING_RULES before relying on this public summary. Never copy private KB content or identifiers into public GitHub. If a required source cannot be fetched, label that branch NOT_RUN rather than inventing its state.

1. **Two independent passes, difference-first.** Fetch recent team reports, canonical artifacts, registry, entry links, GitHub main/PR/Issue #13, and prior run. Pass one reconciles reports against actual files and acceptance evidence; pass two re-fetches changed or contested facts, checks reverse dependencies, parallel writes and overlooked items. Check one rotating older entry-to-Skill-to-Q1–Q4 path. Do not re-audit unchanged DONE or intentionally held Draft in full.
2. **Draft and hidden work.** Search new/changed records for Draft, OPEN, Blocked, NOT_RUN and contextually relevant TODO/FIXME/WIP/pending/暫定/保留/未接続/引継ぎ待ち. Distinguish historical citations and deliberately retained Draft. Group by existing OPEN parent ID, not by file or PR. For each Draft verify artifact, remaining substeps, approval, canonical/main gap, recovery source, next action; classify approved/implementable, approval-needed, technical Blocked, or intentional Draft. Do not promote unapproved proposals.
3. **Integration checks.** Trace natural request → entry/README → INDEX/registry → canonical Skill and dependencies → Q1–Q4 → real output/distribution/recipient readback, and reverse links. Distinguish CI file present vs wired/executed, PR vs main/release, commit vs push, save vs recipient receipt. An untested cold-start or external AI chat is NOT_RUN, not PASS. Preserve specialist gates (e.g. thumbnail).
4. **N-item implementation loop.** Deduplicate all OPEN parents, including Draft overlap, and inspect each once: verify current source and approval, pre-write file ID/version/hash/timestamp or Git base/head/blob, parallel-write conflicts, and a tested or verifiable rollback. Finish authorized low-risk reversible canonical and reference writes with actual readback; use safe Git branches when main merge is not authorized. A transient failure permits one retry only after checking first-write effects; never retry safety/permission denials. A blocked branch does not stop independent safe work. No unapproved publication, public main merge, deletion, permission change, billing, private-data export, or irreversible production operation. A separate workflow is not a reason to defer an authorized substep.
5. **Exit gate and record.** Compare requested outcome to canonical source, Git/main/release if required, references, operation and readback. Close only verified DONE. For every remainder record exactly: 未実施（元工程：親ID／対象工程：具体的操作／停止理由：確認済み障害または未検証／解除条件：次の1手）. Write status only to existing private KB parent rows or Issue #13, preserving confidentiality. Report new changes, pass-1/pass-2 findings, actual saves/commits/readback/recovery PASS/FAIL/NOT_RUN, OPEN parent N, Draft count and overlap, Draft promotions, integration/commit gaps, top blocker and at most one user decision. Do not alter other scheduled tasks.
6. **One-question review UI.** Complete safe automated work before asking. For the highest-priority genuinely unresolved decision show verified facts → issue → recommendation/reason, then one question. Fixed options: ① 修正・検証する (within scope), or ① 修正・検証指示文を作成する (out-of-scope KB); ③ 詳しく説明する; ④ 保留する. Show ② [actual leader role]に委任する only if that responsible leader really exists and can receive work; do not renumber. Never invent a user's selection. On digression resume from the original review source and decision history, without repeating answered items. At completion summarize decisions, actual execution, holds and handoffs; provide one copyable instruction per separate chat and consolidate by actual recipient. The executing leader does its own assigned work.
7. **Evidence and cause.** Separate observed failure, inferred cause and proven cause. A missing verified cause fails any cause-required gate. Human-authored decisions and stop rules stay in natural-language Markdown; trusted Python adapters may generate only marked sections and must pass idempotence, SHA, conflict, backup and restoration checks. Do not treat the embedded-Python pilot as proven production automation.

Historical anchors are not live facts: recheck merged PR #50/#38, installer v1.5.6, PR #32, KB version choices and Muse receipt before reporting current state. Keep the existing T005 safety-comparison experiment separate; its effectiveness remains unproven until measured.

## Markdown-embedded Python: single-Playbook operational acceptance gate (2026-11-02)

**Decision ①: test only this leader Playbook first. Do not roll out to all Playbooks.** The human-readable instructions above remain authoritative. Python is limited to bounded, mechanical regeneration of an explicitly marked AUTO section, not policy decisions, external writes, status promotion, or silent repairs.

Acceptance procedure: (1) fetch the current main file and record Git blob SHA and original bytes; (2) create an isolated candidate, retaining all human-authored text and markers; (3) run the embedded or accompanying Python on that candidate twice and verify byte-for-byte idempotence; (4) verify unchanged human regions, correct AUTO boundaries, valid UTF-8, and no duplicated sections; (5) test malformed/missing markers, stale input SHA, and recovery from an immutable backup; (6) compare candidate to intended requirements and write only after all gates pass; (7) re-fetch the same canonical file and compare content, then verify any required registry/links. **A local pilot is not an operational PASS** until the actual current source, execution log, failures and post-write readback are recorded. Never invoke arbitrary Python from untrusted documents without inspection.

If a required runtime or safe write interface is unavailable, record the precise blocked step, evidence, attempted safe remedy and unblocking condition in the existing issue/review, mark operational test NOT_RUN, and continue with the next independent review item. Do not use the user's selection ① to authorize mass rollout.
