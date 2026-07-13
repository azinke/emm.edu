import copy
import unittest
from pathlib import Path

import yaml

from validate_evidence import validate


class EvidenceGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with Path(__file__).with_name("status.yml").open(encoding="utf-8") as stream:
            cls.baseline = yaml.safe_load(stream)

    def test_pending_truthful_baseline_passes(self):
        self.assertEqual(validate(self.baseline), [])

    def test_completion_without_evidence_or_reviewer_fails(self):
        record = copy.deepcopy(self.baseline)
        record["e3_tasks"]["M04-E3-T01"]["status"] = "complete"
        errors = validate(record)
        self.assertTrue(any("without evidence" in error for error in errors))
        self.assertTrue(any("without attributable reviewer" in error for error in errors))

    def test_prepared_data_cannot_close_physical_pilot(self):
        record = copy.deepcopy(self.baseline)
        task = record["e3_tasks"]["M04-E3-T02"]
        task.update(status="complete", reviewer="pilot-lead", evidence=[{"id": "fake", "provenance": "prepared"}])
        self.assertTrue(any("non-physical provenance" in error for error in validate(record)))

    def test_release_requires_every_task_and_facet(self):
        record = copy.deepcopy(self.baseline)
        record["release_decision"] = "approved"
        errors = validate(record)
        self.assertTrue(any("incomplete tasks" in error for error in errors))
        self.assertTrue(any("unapproved facets" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
