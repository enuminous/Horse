from benchmark import good_case, degraded_case
from horse import HorseEvaluator

if __name__ == "__main__":
    ev = HorseEvaluator()
    good = ev.evaluate(*good_case())
    bad = ev.evaluate(*degraded_case())

    print("full good:", good["joint_effectiveness"])
    print("full degraded:", bad["joint_effectiveness"])

    print("trust-only good:", 1-good["trust_calibration_error"])
    print("trust-only degraded:", 1-bad["trust_calibration_error"])
