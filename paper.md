# HORSE: Human–Operational Recursive System Evaluation

## Abstract

HORSE is an experimental framework for evaluating coupled human–machine operations. It measures trust calibration, handoff integrity, workload balance, intervention quality, latency, and joint task effectiveness while preserving the recursive interaction history between human and system.

## 1. Motivation

Evaluating humans and automation separately can miss failures that arise only through interaction.

A highly capable system can still fail operationally if:
- trust is miscalibrated,
- handoffs are poor,
- workload spikes,
- intervention arrives too late,
- responsibility is unclear.

## 2. Model

Coupled state:

`z_t=(x_t,h_t)`

Trust calibration error:

`T=|human_trust-system_reliability|`

Handoff integrity:

`H=preserved_elements/required_elements`

Workload penalty:

`W=f(workload,attention,fatigue)`

Joint effectiveness:

`J=alpha*success+beta*H+gamma*(1-T)-delta*W+epsilon*intervention_quality`

## 3. Metrics

- joint task effectiveness
- trust calibration
- handoff integrity
- intervention quality
- intervention latency
- workload penalty
- recursive team coherence

## 4. Baselines

- human-only performance
- automation-only performance
- static trust measures
- standard human-factors workload metrics
- simple handoff completion rates

## 5. Ablations

- remove trust calibration
- remove handoff integrity
- remove workload
- remove intervention quality
- remove interaction history
- evaluate human and system independently

## 6. Falsification

If isolated human and system metrics predict team outcomes equally well, HORSE's coupled-state formulation is not justified.

## 7. Claim boundary

HORSE evaluates operational interaction. It does not infer hidden mental states, subjective experience, or consciousness.
