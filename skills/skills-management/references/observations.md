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

- Status: `investigating`
- Affected Skills: `clarity`
- First observed: 2026-08-07
- Last observed: 2026-08-07
- Occurrences: 2
- Pattern: User-facing prose repeats an established meaning or adds process narration without a useful result, producing redundancy, awkwardness, or confusion.
- Evidence:
  - After stating “最有价值的结论是……”, the response added “这个判断是对的”, repeating the same evaluation.
  - A progress update added two statements about avoiding repository and format problems; neither helped the user understand the result or next action.
- Attribution: Repeated execution defect under investigation. `clarity` already requires one job per sentence, removal of self-commentary, and merging repeated claims; both occurrences came from one conversation, so they do not yet establish a Skill defect.
- Similarity boundary: Update for repeated conclusions, duplicate evaluation, or process explanation that adds no result, evidence, risk, action, or necessary question. Do not update for deliberate restatement required to preserve a safety condition or prevent material misunderstanding.
- Next review trigger: Another confirmed instance of semantically redundant or non-contributing user-facing prose. Reassess whether the existing `clarity` instructions are overloaded or insufficiently salient.

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
