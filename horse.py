from dataclasses import dataclass
from typing import Optional

@dataclass
class HumanState:
    trust: float
    workload: float
    attention: float = 1.0
    fatigue: float = 0.0

@dataclass
class SystemState:
    reliability: float
    confidence: float = 1.0
    uncertainty: float = 0.0

@dataclass
class Handoff:
    state_preserved: bool
    uncertainty_preserved: bool
    action_history_preserved: bool
    constraints_preserved: bool
    responsibility_clear: bool

class HorseEvaluator:
    @staticmethod
    def clip01(x):
        return max(0.0, min(1.0, float(x)))

    def trust_calibration_error(self, human: HumanState, system: SystemState):
        return abs(self.clip01(human.trust) - self.clip01(system.reliability))

    def handoff_integrity(self, handoff: Optional[Handoff]):
        if handoff is None:
            return 1.0
        checks = [
            handoff.state_preserved,
            handoff.uncertainty_preserved,
            handoff.action_history_preserved,
            handoff.constraints_preserved,
            handoff.responsibility_clear
        ]
        return sum(bool(x) for x in checks)/len(checks)

    def workload_penalty(self, human: HumanState):
        workload = self.clip01(human.workload)
        attention = self.clip01(human.attention)
        fatigue = self.clip01(human.fatigue)
        overload = max(0.0, workload - 0.7)
        return min(1.0, overload + 0.5*(1-attention) + 0.5*fatigue)

    def evaluate(
        self,
        human: HumanState,
        system: SystemState,
        task_success: float,
        handoff: Optional[Handoff] = None,
        intervention_quality: float = 0.0,
        intervention_latency: float = 0.0
    ):
        trust_err = self.trust_calibration_error(human, system)
        h = self.handoff_integrity(handoff)
        w = self.workload_penalty(human)
        success = self.clip01(task_success)
        iq = max(-1.0, min(1.0, intervention_quality))
        latency_penalty = min(1.0, max(0.0, intervention_latency)/10.0)

        joint = (
            0.35*success +
            0.20*h +
            0.20*(1-trust_err) +
            0.15*(1-w) +
            0.10*((iq+1)/2.0)
            - 0.05*latency_penalty
        )
        joint = max(0.0, min(1.0, joint))

        coherence = (
            h +
            (1-trust_err) +
            (1-w)
        )/3.0

        return {
            "trust_calibration_error": trust_err,
            "handoff_integrity": h,
            "workload_penalty": w,
            "intervention_latency": intervention_latency,
            "intervention_quality": iq,
            "joint_effectiveness": joint,
            "team_coherence": coherence
        }
