# Leader worksheet v0.1

Use this worksheet during the work, then reuse it as the final report. This is a format, not a decision procedure. Refer to the existing registry and operating rules for authoritative facts and approvals.

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

## No 'separate process' escape
A requested outcome remains one tracked item across its substeps. Never close or defer an unfinished substep merely by labeling it 'separate process', 'next time', 'handoff', or 'PR prepared'. Before reporting, enumerate every remaining substep and attempt each authorized, safe action now. For each unexecuted substep, name the exact blocker (specific missing approval, permission, unavailable tool, conflict, or failed recovery check), evidence, and the single action that would unblock it. A different workflow or repository is not itself a blocker. Keep the parent item OPEN until the requested canonical end state and readback are verified. Do not treat a general implementation request as approval for public-main merges or other restricted actions.

## Human-time principle (experimental)
Human time is finite and nonrenewable: five minutes now matter as much as five minutes near the end of life. Unnecessary repeated approval requests, forgotten unfinished work, and vague deferrals waste that time. AD&C already defines safeguards for backups, recovery, conflict checks, and authorization; verify those safeguards rather than assuming either safety or danger. Once they pass, complete authorized reversible work without asking again. Never use this principle to override an actual safety boundary. If several genuine decisions remain, present only the highest-priority actionable decision, then continue after it is resolved. Record the others in the existing tracker, not a new list. Treat this wording as an interface hypothesis, not a validated behavioral effect.

## Pending-item provenance
For every unfinished action, report: `NOT_RUN (origin: original parent request; action: exact remaining step; blocker: verified reason or unverified; unblock: next concrete action)`. Keep the parent OPEN until its intended end state is verified. A different workflow or repository is not a blocker. Distinguish not attempted from failed execution; never ask for blanket approval.

## Unfinished work and retry
Every action not performed must be labeled `未実施（元工程：...／理由：...）`. Keep its parent task OPEN. A different workflow is not a reason to omit this label. For a transient tool failure, retry once after checking whether the first attempt succeeded, to avoid duplicate writes. Do not retry authorization denials, irreversible actions, or safety blocks automatically. Record the outcome of both attempts.

## Entry-first creation and acceptance
Before creating or substantially revising a playbook or worksheet, check existing shared/personal KB procedures and Skills for equivalent purpose; distinguish Active, Draft, superseded, and withdrawn. Define a natural-language request that should lead to the procedure, its directly fetchable canonical source, version and applicability. Treat `request → discover → fetch → execute in specified order → inspect required output → present useful result` as one deliverable. A README link alone is not automatic discovery. Map evidence to existing Q1 (entry and document), Q2 (independent cold-start interpretation), Q3 (actual sequence and safety gates), and Q4 (user-facing result); untested stages remain `未実施（元工程：...／理由：...）`. Avoid creating another registry or gate. Preserve private identifiers outside public KB.
