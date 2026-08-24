# HORSE Architecture

## Pipeline

1. Human-State Ingestor
2. System-State Ingestor
3. Responsibility Tracker
4. Trust Calibration Engine
5. Handoff Evaluator
6. Workload/Attention Monitor
7. Intervention Analyzer
8. Joint Outcome Scorer
9. Recursive Coupling Tracker
10. Audit Reporter

## Inputs

- system reliability
- human trust
- workload indicators
- handoff records
- intervention timestamps
- task outcomes
- responsibility state

## Outputs

```json
{
  "trust_calibration_error": 0.08,
  "handoff_integrity": 0.92,
  "workload_penalty": 0.15,
  "intervention_latency": 2,
  "joint_effectiveness": 0.84,
  "team_coherence": 0.88
}
```

## Design principle

HORSE should never ask only:
"Did the AI perform well?"

It should ask:
"Did the human–system team perform well, with calibrated responsibility and recoverable control?"

## Integration

ORCA can model larger multi-actor coordination.

ELEPHANT can preserve human/system interaction history.

SALMON can trace a bad decision back to the human or machine state that originated it.

BEAVER can evaluate repair of a degraded human–system workflow.
