from __future__ import annotations

import unittest

from curriculum.scripts.plan_lab_inventory import calculate


CATALOG = {
    "items": [
        {"id": "BOARD", "name_en": "board", "name_fr": "carte", "class": "personal", "ratio": 1, "spare_fraction": 0.15, "deliberate_fault_reserve": 0},
        {"id": "SCOPE", "name_en": "scope", "name_fr": "oscilloscope", "class": "simultaneous-pair", "ratio": 2, "spare_fraction": 0.15, "deliberate_fault_reserve": 1},
    ]
}


class InventoryPlanTests(unittest.TestCase):
    def setUp(self) -> None:
        self.plan = {
            "status": "approved-cohort",
            "cohort_id": "COHORT-2027-A",
            "deployment_profile": "DP-TEST",
            "enrolled_students": 25,
            "largest_section": 17,
            "pair_size": 2,
            "rotations": 1,
            "qualified_rooms": 1,
            "serviceable_on_hand": {"BOARD": 2},
            "accepted_on_order": {"BOARD": 1},
        }

    def test_rounding_spares_reserve_and_stock(self) -> None:
        result = calculate(self.plan, CATALOG)
        board, scope = result["items"]
        self.assertEqual(board["gross_requirement"], 29)
        self.assertEqual(board["planned_order_quantity"], 26)
        self.assertEqual(scope["base_quantity"], 9)
        self.assertEqual(scope["gross_requirement"], 12)

    def test_planning_scenario_is_rejected_by_default(self) -> None:
        self.plan["status"] = "planning-scenario"
        with self.assertRaisesRegex(ValueError, "not approved"):
            calculate(self.plan, CATALOG)

    def test_planning_scenario_can_be_explicitly_modelled(self) -> None:
        self.plan["status"] = "planning-scenario"
        result = calculate(self.plan, CATALOG, allow_planning_scenario=True)
        self.assertEqual(result["evidence_status"], "planning-scenario-not-procurement-evidence")

    def test_invalid_capacity_input_fails(self) -> None:
        self.plan["largest_section"] = 26
        with self.assertRaisesRegex(ValueError, "cannot exceed"):
            calculate(self.plan, CATALOG)


if __name__ == "__main__":
    unittest.main()

