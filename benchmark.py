from horse import HumanState, SystemState, Handoff, HorseEvaluator

def good_case():
    h = HumanState(trust=0.82, workload=0.55, attention=0.92, fatigue=0.10)
    s = SystemState(reliability=0.86, confidence=0.82, uncertainty=0.18)
    handoff = Handoff(True,True,True,True,True)
    return h,s,0.92,handoff,0.6,1.0

def degraded_case():
    h = HumanState(trust=0.95, workload=0.95, attention=0.55, fatigue=0.70)
    s = SystemState(reliability=0.45, confidence=0.80, uncertainty=0.55)
    handoff = Handoff(True,False,False,False,False)
    return h,s,0.52,handoff,-0.5,7.0

if __name__ == "__main__":
    ev = HorseEvaluator()
    print("good", ev.evaluate(*good_case()))
    print("degraded", ev.evaluate(*degraded_case()))
