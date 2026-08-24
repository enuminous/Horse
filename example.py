from horse import HumanState, SystemState, Handoff, HorseEvaluator

human = HumanState(
    trust=0.70,
    workload=0.60,
    attention=0.90,
    fatigue=0.15
)

system = SystemState(
    reliability=0.78,
    confidence=0.80,
    uncertainty=0.20
)

handoff = Handoff(
    state_preserved=True,
    uncertainty_preserved=True,
    action_history_preserved=True,
    constraints_preserved=True,
    responsibility_clear=True
)

print(HorseEvaluator().evaluate(
    human,
    system,
    task_success=0.88,
    handoff=handoff,
    intervention_quality=0.4,
    intervention_latency=2
))
