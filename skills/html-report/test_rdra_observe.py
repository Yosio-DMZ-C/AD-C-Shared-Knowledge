import unittest
from rdra_observe import analyze, SCHEMA

class ObserveTests(unittest.TestCase):
    def test_expected_candidates_and_unconfirmed(self):
        d=analyze({"schema":SCHEMA,"relations":[{"id":"bad","expected":"a","observed":"b"},{"id":"missing","expected":"a"},{"id":"ok","expected":"a","observed":"a"}]})
        self.assertEqual([(x["id"],x["kind"]) for x in d["findings"]],[("bad","relation_mismatch"),("missing","unconfirmed")])
    def test_completion_evidence_and_recovery(self):
        d=analyze({"schema":SCHEMA,"events":[{"id":"x","state":"waiting","completed":True},{"id":"y","state":"success","completed":True,"evidence":["ref"]}]})
        self.assertEqual({x["kind"] for x in d["findings"]},{"completion_state_mismatch","completion_without_evidence","recovery_path_missing"})
    def test_management_candidate_only_when_explicit(self):
        d=analyze({"schema":SCHEMA,"events":[{"id":"m","state":"done","work_type":"management","purpose_contribution":False}]})
        self.assertEqual([x["kind"] for x in d["findings"]],["management_value_unclear"])
    def test_rejects_wrong_schema(self):
        with self.assertRaises(ValueError): analyze({"schema":"wrong"})

if __name__ == "__main__": unittest.main()
