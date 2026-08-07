# Refactor Review Checklist

## Scope

- Does the diff only contain the requested refactor?
- Are unrelated cleanups separated?
- Are mechanical changes separated from semantic changes?
- Is each step reversible?

## Behavior

- What behavior is preserved?
- Which tests prove it?
- Are public APIs, configs, protocols, metrics, logs, and errors unchanged?
- Are edge cases and failure paths preserved?

## Design

- Does the refactor reduce complexity?
- Does it improve information hiding?
- Does it remove or add shallow wrappers?
- Does it reduce change amplification?
- Are ownership and lifecycle clearer?

## Risk

- Could callers observe behavior changes?
- Could generated code or external automation break?
- Could performance change materially?
- Is rollback simple?
