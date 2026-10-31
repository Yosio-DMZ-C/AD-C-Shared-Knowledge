# Leader worksheet v0.1

Use this worksheet during the work, then reuse it as the final report. This is a format, not a decision procedure. Refer to the existing registry and operating rules for authoritative facts and approvals.

**Execution model (2026-10-29 β):** Team members complete their authorized reversible changes through canonical writes, reference/Git integration and readback; the leader audits across changes and repairs scoped inconsistencies. Keep the existing three daily scheduled reviews and two-pass audit; this worksheet does not reschedule or weaken them. Audit significant dependencies and actual restorability, not just reported completion. Avoid new trackers and duplicate approval prompts.

1. New changes: record only new facts, or 'no new changes'.
2. Reconciliation: note sources checked, discrepancies, and unverified claims.
3. Implementation: record actual writes, commits, readback, and PASS / FAIL / NOT_RUN.
4. Recovery: identify prior version and whether rollback was actually tested.
5. Next action: one priority and, if needed, one approval question.

Keep routine reports brief. Mark irrelevant checks N/A with a reason. Never report a draft or unverified change as DONE.

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

## One-shot worker handoff: execute, do not paraphrase (β)

For a handoff through a scheduled one-time task, record a concrete **parent task ID, origin request timestamp (with timezone), origin chat reference if accessible, canonical KB task/Context reference, already-approved scope, completion evidence, and the existing KB result destination** in the worker's actual prompt. The worker must **attempt to read the origin conversation around that instruction timestamp when supported**, reconcile it with the canonical KB handoff, then **perform the authorized work** and read back the saved result. Merely summarizing the chat, creating a Draft, or handing the instruction back to the user is NOT execution. If chat access is unavailable, mark origin-chat NOT_RUN (do not invent the dialogue) and continue independently safe tasks when the KB contains sufficient instructions and authorization. If essential details are missing, stop only the affected step and record its exact blocker. Verify child execution, KB write/readback, parent reception, and worker self-disable separately; never claim a disabled task was deleted or that a new child chat is automatically attached to its parent. Preserve approval, recovery, conflict and privacy boundaries; do not create a second tracker.

## Entry-first creation and acceptance
Before creating or substantially revising a playbook or worksheet, check existing shared/personal KB procedures and Skills for equivalent purpose; distinguish Active, Draft, superseded, and withdrawn. Define a natural-language request that should lead to the procedure, its directly fetchable canonical source, version and applicability. Treat `request → discover → fetch → execute in specified order → inspect required output → present useful result` as one deliverable. A README link alone is not automatic discovery. Map evidence to existing Q1 (entry and document), Q2 (independent cold-start interpretation), Q3 (actual sequence and safety gates), and Q4 (user-facing result); untested stages remain `未実施（元工程：...／理由：...）`. Avoid creating another registry or gate. Preserve private identifiers outside public KB.
