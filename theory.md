# HORSE Theory

## 1. Problem

Human–machine systems fail in relational ways.

Typical failures include:
- overtrust,
- undertrust,
- automation surprise,
- poor handoff timing,
- unclear responsibility,
- workload spikes,
- ignored warnings,
- unnecessary overrides,
- delayed intervention.

HORSE treats the human–system pair as the unit of analysis.

## 2. Coupled state

Let system state be:

`x_t`

and human operational state be:

`h_t`

The coupled team state is:

`z_t = (x_t, h_t)`

## 3. Trust calibration

Let system reliability estimate be:

`r_t in [0,1]`

and human trust be:

`q_t in [0,1]`

Trust calibration error:

`T_t = |q_t - r_t|`

Lower is better.

## 4. Override quality

An override is useful if it improves outcome relative to leaving automation unchanged.

For intervention `a_h`:

`O = Outcome(with_override) - Outcome(no_override)`

A harmful override has negative `O`.

## 5. Handoff integrity

A handoff should preserve:
- current state,
- uncertainty,
- action history,
- active constraints,
- responsibility.

Candidate handoff score:

`H = preserved_required_elements / total_required_elements`

## 6. Workload balance

Let human workload be `W_h` and system workload be `W_s`.

The relevant question is not equal load, but whether critical tasks are allocated to the actor currently best positioned to perform them.

## 7. Intervention latency

If intervention becomes necessary at `T_need` and occurs at `T_act`:

`L_int = T_act - T_need`

Both premature and delayed intervention can be costly.

## 8. Joint effectiveness

Candidate score:

`J = alpha*task_success + beta*H + gamma*(1-T) - delta*workload_penalty - epsilon*intervention_cost`

## 9. Recursive coupling

Human trust and system behavior influence each other:

`q_{t+1} = G(q_t, observed_performance_t, explanation_t)`

`x_{t+1} = F(x_t, human_action_t, environment_t)`

HORSE explicitly models this feedback loop.

## 10. EFMW interpretation

The EFMW-inspired aspect is the recursive relational state across human and machine.

The unit is not:
- human,
or
- AI.

It is the **operational coupling between them**.

## 11. Falsifiable prediction

HORSE should add value when:
- responsibility shifts dynamically,
- trust evolves,
- interventions matter,
- handoffs occur,
- workload changes.

If isolated human and system metrics predict outcomes equally well, HORSE's added structure is not justified.
