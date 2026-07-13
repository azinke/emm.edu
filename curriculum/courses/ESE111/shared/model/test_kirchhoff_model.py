import unittest

from kirchhoff_model import corner_ranges, solve


class KirchhoffModelTests(unittest.TestCase):
    def test_nominal_solution_and_balances(self):
        result = solve()
        self.assertAlmostEqual(result.tp_a_v, 3.6082004556, places=9)
        self.assertAlmostEqual(result.tp_b_v, 1.1275626424, places=9)
        self.assertLess(abs(result.kcl_a_residual_a), 1e-15)
        self.assertLess(abs(result.kcl_b_residual_a), 1e-15)
        self.assertLess(abs(result.power_balance_residual_w), 1e-15)

    def test_meter_loading_is_visible_and_conserved(self):
        unloaded = solve()
        loaded = solve(meter_b_ohm=1_000_000.0)
        self.assertLess(loaded.tp_b_v, unloaded.tp_b_v)
        self.assertGreater(loaded.i_meter_a, 0.0)
        self.assertLess(abs(loaded.kcl_b_residual_a), 1e-15)

    def test_redesign_meets_requirement_at_declared_corners(self):
        ranges = corner_ranges(22_000.0)
        self.assertGreaterEqual(ranges["tp_b_v"][0], 1.40)
        self.assertLessEqual(ranges["tp_b_v"][1], 1.52)
        self.assertLessEqual(ranges["i_r1_a"][1], 0.00025)

    def test_baseline_fails_changed_threshold(self):
        ranges = corner_ranges(15_000.0)
        self.assertLess(ranges["tp_b_v"][1], 1.40)

    def test_invalid_resistance_rejected(self):
        with self.assertRaises(ValueError):
            solve(r3=0.0)


if __name__ == "__main__":
    unittest.main()

