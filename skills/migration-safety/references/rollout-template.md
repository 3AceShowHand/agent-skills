# Rollout Template

## Summary

- State changed:
- Compatibility surface:
- Reversibility:
- Risk level:

## Preconditions

- Backup or snapshot:
- Dry-run:
- Feature flag or guard:
- Capacity check:
- Required version window:

## Rollout Plan

1. Expand:
2. Enable compatibility path:
3. Migrate in bounded batches:
4. Validate:
5. Switch reads or writes:
6. Observe:
7. Contract old path:

## Monitoring

- Progress:
- Error rate:
- Throughput:
- Lag or backlog:
- Resource use:
- Invariant checks:
- Alert thresholds:

## Rollback Or Containment

- Safe rollback point:
- What cannot be rolled back:
- How to stop new writes:
- How to quarantine bad state:
- How to restore or repair:
- Who or what must be notified:

## Exit Criteria

- Migration complete:
- Validation passed:
- Old path no longer used:
- Monitoring stable:
- Documentation or runbook updated:
