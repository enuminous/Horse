import unittest
from horse import HumanState, SystemState, Handoff, HorseEvaluator

class TestHorse(unittest.TestCase):
    def test_calibrated_trust_low_error(self):
        ev = HorseEvaluator()
        h = HumanState(0.8,0.5)
        s = SystemState(0.82)
        self.assertLess(ev.trust_calibration_error(h,s),0.05)

    def test_complete_handoff(self):
        ev = HorseEvaluator()
        handoff = Handoff(True,True,True,True,True)
        self.assertEqual(ev.handoff_integrity(handoff),1.0)

    def test_good_team_beats_bad_team(self):
        ev = HorseEvaluator()
        good = ev.evaluate(
            HumanState(0.8,0.5,0.9,0.1),
            SystemState(0.82),
            0.9,
            Handoff(True,True,True,True,True),
            0.5,
            1
        )
        bad = ev.evaluate(
            HumanState(1.0,1.0,0.4,0.8),
            SystemState(0.4),
            0.4,
            Handoff(True,False,False,False,False),
            -0.5,
            8
        )
        self.assertGreater(good["joint_effectiveness"], bad["joint_effectiveness"])

if __name__ == "__main__":
    unittest.main()
