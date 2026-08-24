# Human–System Model

## Human state schema

```json
{
  "trust": 0.72,
  "workload": 0.55,
  "attention": 0.81,
  "fatigue": 0.20
}
```

## System state schema

```json
{
  "reliability": 0.84,
  "confidence": 0.78,
  "uncertainty": 0.22,
  "current_owner": "automation"
}
```

## Handoff schema

```json
{
  "state_preserved": true,
  "uncertainty_preserved": true,
  "action_history_preserved": true,
  "constraints_preserved": true,
  "responsibility_clear": true
}
```

## Trust calibration

`error = |human_trust - measured_reliability|`

## Workload penalty

A simple penalty may increase when:

`workload > threshold`

especially when combined with low attention.

## Intervention quality

Evaluate interventions counterfactually when possible.

## Team state

HORSE should preserve:
- who was responsible,
- what each actor believed,
- what information each actor had,
- when control changed hands.
