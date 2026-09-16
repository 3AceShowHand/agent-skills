# Skill Evolution Observations

This journal retains active, user-confirmed evidence that may become relevant when similar agent errors recur. An observation is evidence for later attribution, not a requirement or an automatic reason to change a Skill.

## Maintenance Rules

### Add or update

- Record only explicit user corrections or objective outcomes. Do not record agent self-assessment alone.
- Create a new entry only when no active observation covers the same behavior and likely cause.
- For a similar error, update the existing entry: increment `Occurrences`, update `Last observed`, add only the minimum new evidence, and reassess the attribution.
- Judge similarity from behavior, impact, and likely cause. Exact wording, task, and identifier matches are unnecessary.
- Treat recurrence as a reason to investigate instruction ambiguity or overload. Counts trigger investigation, not a Skill-defect conclusion.

### Escalate

Use these states:

- `observing`: Retain the first confirmed occurrence when an execution defect, task-specific exception, or model variance remains plausible.
- `investigating`: Reassess the governing instructions after a similar error recurs, or after one occurrence directly exposes a missing, ambiguous, conflicting, or unusable instruction.
- `escalated`: Use only after the investigation attributes the error to a Skill defect or routing defect and identifies a reusable correction with a clear boundary.

Move an observation from `observing` to `investigating` when either condition holds:

- two or more confirmed similar errors share the same behavior and likely cause;
- one confirmed error directly shows that a required instruction or source of truth is missing, ambiguous, conflicting, or impossible to follow.

Recurrences from independent tasks, conversations, or agents are stronger evidence than repeated errors in one conversation. Do not require independence before investigating.

Move an observation to `escalated` only when all applicable checks pass:

- the affected Skill was loaded and relevant to the failed behavior;
- evidence identifies a missing, ambiguous, conflicting, overloaded, or incorrectly routed instruction;
- task-specific preference and unexplained model variance do not adequately explain the error;
- the correction generalizes beyond the observed wording or task;
- a boundary and representative counterexample show when the correction should not apply;
- a minimal Skill change can plausibly prevent the error without weakening correct behavior.

After escalation, report the attribution, generalized principle, affected scope, counterexample, and proposed change. Modify the Skill only after user confirmation. A validated and released change clears the observation.

### Clear

Keep only active observations. Delete an entry when any of these conditions holds:

- a validated and released Skill change resolves it;
- later evidence disproves the attribution;
- the user withdraws or corrects the observation;
- it is task-specific and has no reusable value;
- it has been merged into a broader observation.

On every update, merge overlapping entries, remove cleared entries, and trim evidence to the smallest representative examples. Do not clear an unresolved observation only because time has passed. Git history retains removed records.

### Entry fields

- `ID`: stable name for the behavior pattern, not an exact output string.
- `Status`: `observing`, `investigating`, or `escalated`.
- `Affected Skills`: Skills that governed the behavior.
- `First observed` and `Last observed`: ISO dates.
- `Occurrences`: number of confirmed similar errors represented by the entry.
- `Pattern`: reusable description of the error.
- `Evidence`: minimum representative input, output, and correction.
- `Attribution`: current classification and supporting reason.
- `Similarity boundary`: what should and should not update this entry.
- `Next review trigger`: evidence that should cause re-evaluation.

## Active Observations

### redundant-expression-causing-language-error

- Status: `escalated`
- Affected Skills: `clarity`
- First observed: 2026-08-07
- Last observed: 2026-08-19
- Occurrences: 4
- Pattern: User-facing prose repeats an established meaning, adds process narration without a useful result, or uses a reject-X/assert-Y frame where direct claims would be clearer.
- Evidence:
  - After stating “最有价值的结论是……”, the response added “这个判断是对的”, repeating the same evaluation.
  - A progress update added two statements about avoiding repository and format problems; neither helped the user understand the result or next action.
  - A technical explanation introduced an ownership conclusion through a reject-X/assert-Y frame; the user assigned this construction a zero score and prohibited it from user-visible output.
  - A document principle stated independence from an output mechanism, then appended its direct implication; the user identified the trailing explanation as redundant.
- Attribution: Confirmed Skill defect. `clarity` conditionally permitted contrast while an example discouraged one instance, leaving a permissive rule that repeatedly allowed low-value framing. The confirmed correction replaces that ambiguity with a hard structural gate.
- Similarity boundary: Update for repeated conclusions, duplicate evaluation, non-contributing process explanation, or adversative correction framing. Exclude deliberate repetition needed to preserve a safety condition; express that repetition through direct statements.
- Next review trigger: Validate the hard gate against direct explanations, material distinctions, and source paraphrases. Clear this observation after the source change is released to its intended agents.

### evolve-analysis-reported-as-skill-list

- Status: `observing`
- Affected Skills: `skills-management`, `clarity`
- First observed: 2026-08-07
- Last observed: 2026-08-07
- Occurrences: 1
- Pattern: The response says that `skills-management` was used but omits the observed problem, attribution, generalized principle, and proposed next action.
- Evidence: The response reported only that `skills-management` analyzed a routing deviation and changed no files; the user asked what problem was found and what would be done.
- Attribution: Execution defect. `skills-management` already requires the missing report fields.
- Similarity boundary: Update when Skill usage is disclosed without the material result required by that Skill. Do not update when the Skill performed no material analysis and a name-only disclosure is all the user requested.
- Next review trigger: Another confirmed omission of required `skills-management` analysis. Reassess whether the reporting contract needs a shorter mandatory template.

### standalone-document-routed-to-code-review

- Status: `observing`
- Affected Skills: `code-review`, `write-great-document`
- First observed: 2026-08-07
- Last observed: 2026-08-07
- Occurrences: 1
- Pattern: A standalone requirements or current-state document review is routed to `code-review` because the request uses the word “review”, despite having no code change, pull request, worktree assessment, or implementation-design review scope.
- Evidence: A request to review `changefeed-traffic-metering.md` triggered `code-review`; the user corrected the routing because the target was a document rather than code.
- Attribution: Routing execution defect. The artifact and requested deliverable were not classified before selecting the Skill.
- Similarity boundary: Update for standalone requirements, current-state, or narrative document reviews incorrectly routed to `code-review`. Do not update for design reviews tied to implementation boundaries, a pull request, or a pre-merge change assessment.
- Next review trigger: Another confirmed document-type misrouting. Reassess whether `code-review` metadata or routing cases leave “design review” too broad.

### split-delivery-consumers-omitted-from-complexity-review

- Status: `investigating`
- Affected Skills: `ponytail-review`, `codebase-navigation`
- First observed: 2026-08-28
- Last observed: 2026-08-28
- Occurrences: 2
- Pattern: A complexity review labels provider APIs as unused or speculative after checking only the current branch, while concrete consumers and orchestration live in linked branches or repositories.
- Evidence:
  - The review proposed deleting SDK capability interfaces because the SDK branch had no local callers; the user identified caselib consumers on the companion `add-kafka-auth` branch.
  - The revised scope included the consumer branch but omitted a registered test-plan YAML that provisions the resources and executes every Kafka security profile, including HTTP OAuth compatibility.
- Attribution: Repeated execution defect under investigation. `codebase-navigation` already requires tracing direct consumers and external contracts, while `ponytail-review` limits findings to the diff without authorizing local-call-count assumptions about an explicitly split delivery.
- Similarity boundary: Update when concrete repository evidence or user-provided context links provider, consumer, and orchestration artifacts across branches or repositories. Exclude nearby branches and repositories connected only by similar names or speculative future plans.
- Next review trigger: Reassess whether either Skill needs an explicit cross-artifact scope check after an independent recurrence, or after a review repeats this error despite having the linked delivery context up front.
