import csv
import json
import unittest
from pathlib import Path

from kirchhoff_model import corner_ranges, solve


class KirchhoffModelTests(unittest.TestCase):
    shared = Path(__file__).resolve().parents[1]

    def test_nominal_solution_and_balances(self):
        result = solve()
        self.assertAlmostEqual(result.tp_a_v, 3.6082004556, places=9)
        self.assertAlmostEqual(result.tp_b_v, 1.1275626424, places=9)
        self.assertLess(abs(result.kcl_a_residual_a), 1e-15)
        self.assertLess(abs(result.kcl_b_residual_a), 1e-15)
        self.assertLess(abs(result.kvl_source_r1_r2_residual_v), 1e-12)
        self.assertLess(abs(result.kvl_r2_r3_r4_residual_v), 1e-12)
        self.assertLess(abs(result.power_balance_residual_w), 1e-15)

    def test_meter_loading_is_visible_and_conserved(self):
        unloaded = solve()
        loaded = solve(meter_b_ohm=1_000_000.0)
        self.assertLess(loaded.tp_b_v, unloaded.tp_b_v)
        self.assertGreater(loaded.i_meter_a, 0.0)
        self.assertLess(abs(loaded.kcl_b_residual_a), 1e-15)
        self.assertLess(abs(loaded.kvl_source_r1_r2_residual_v), 1e-12)
        self.assertLess(abs(loaded.kvl_r2_r3_r4_residual_v), 1e-12)

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

    def test_prepared_data_and_raw_schema_are_reproducible(self):
        with (self.shared / "data" / "prepared-analysis.csv").open(newline="", encoding="utf-8") as handle:
            rows = {(row["run_id"], row["from_node"]): row for row in csv.DictReader(handle)}
        prepared_a = solve(5.98, 9_980.0, 22_100.0, 32_900.0, 14_920.0, 1_000_000.0)
        expected_a = {"VS": 5.98, "TP-A": prepared_a.tp_a_v, "TP-B": prepared_a.tp_b_v}
        for node, expected in expected_a.items():
            self.assertAlmostEqual(float(rows[("PREP-A", node)]["value"]), round(expected, 3), places=3)
        open_r3_a = 5.98 * 22_100.0 / (9_980.0 + 22_100.0)
        self.assertAlmostEqual(float(rows[("PREP-B", "TP-A")]["value"]), round(open_r3_a, 3), places=3)
        self.assertEqual(float(rows[("PREP-B", "TP-B")]["value"]), 0.0)
        self.assertTrue(all(row["coverage_factor"] == "2" for row in rows.values()))

        schema = json.loads((self.shared / "data" / "raw-data.schema.json").read_text(encoding="utf-8"))
        item = schema["properties"]["observations"]["items"]
        self.assertIn("boolean", item["properties"]["value"]["type"])
        continuity = next(branch for branch in item["oneOf"] if branch["properties"]["quantity"].get("const") == "continuity")
        self.assertEqual(continuity["properties"]["unit"]["const"], "boolean")
        self.assertEqual(continuity["properties"]["value"]["type"], "boolean")


if __name__ == "__main__":
    unittest.main()
