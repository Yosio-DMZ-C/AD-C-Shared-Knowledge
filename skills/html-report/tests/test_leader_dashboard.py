import importlib.util
import json
import unittest
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent if Path(__file__).parent.name == "tests" else Path(__file__).parent
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("leader_dashboard", ROOT / "leader_dashboard.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
SAMPLE = json.loads((ROOT / "example_leader_dashboard.synthetic.json").read_text(encoding="utf-8"))


class DashboardTests(unittest.TestCase):
    def test_work60_duplicates_and_old_unknown_are_excluded(self):
        work = next(c for c in mod.normalize(SAMPLE)["categories"] if c["id"] == "work60")
        self.assertEqual(len(work["items"]), 1)
        self.assertEqual(work["states"]["ready"], 1)
        self.assertEqual(work["denominator"], 1)

    def test_missing_denominator_is_not_zero(self):
        self.assertIn("未集計", mod.render(SAMPLE))

    def test_status_counters_are_not_vertically_summed(self):
        html = mod.render(SAMPLE)
        self.assertIn("READY=1件", html)
        self.assertNotIn("件数合計=", html)

    def test_sent_only_does_not_turn_into_done(self):
        data = json.loads(json.dumps(SAMPLE))
        data["categories"][1]["items"] = [{"id": "FAKE-SENT", "parent_id": "P", "status": "SENT"}]
        work = next(c for c in mod.normalize(data)["categories"] if c["id"] == "work60")
        self.assertEqual(work["states"]["sent"], 1)
        self.assertEqual(work["states"]["done"], 0)
        self.assertEqual(work["denominator"], 1)

    def test_conflicting_duplicate_state_is_rejected(self):
        data = json.loads(json.dumps(SAMPLE))
        data["categories"][1]["items"] = [
            {"id": "SAME", "parent_id": "P", "status": "READY"},
            {"id": "SAME", "parent_id": "P", "status": "DONE"},
        ]
        with self.assertRaisesRegex(ValueError, "conflicting duplicate state"):
            mod.normalize(data)

    def test_distinct_parent_and_id_pairs_remain_distinct(self):
        data = json.loads(json.dumps(SAMPLE))
        data["categories"][1]["items"] = [
            {"id": "SAME", "parent_id": "P1", "status": "READY"},
            {"id": "SAME", "parent_id": "P2", "status": "SENT"},
        ]
        work = next(c for c in mod.normalize(data)["categories"] if c["id"] == "work60")
        self.assertEqual(work["denominator"], 2)
        self.assertEqual(len(work["items"]), 2)

    def test_unsaved_or_missing_data_remains_unknown(self):
        data = json.loads(json.dumps(SAMPLE))
        data["categories"][0]["items"] = [{"id": "FAKE-X", "title": "X", "status": "未確認"}]
        out = mod.render(data)
        self.assertIn("未確認", out)

    def test_untrusted_html_and_non_https_links_are_not_active(self):
        data = json.loads(json.dumps(SAMPLE))
        data["categories"][0]["items"][0]["title"] = "<script>alert(1)</script>"
        data["categories"][0]["items"][0]["source_url"] = "javascript:alert(1)"
        out = mod.render(data)
        self.assertNotIn("<script>alert(1)</script>", out)
        self.assertNotIn('href="javascript:', out)

    def test_renderer_keeps_meta_header_filters_copy_and_source_links(self):
        out = mod.render(SAMPLE)
        self.assertIn("リーダーダッシュボード", out)
        self.assertIn("取得時点", out)
        self.assertIn("data-filter", out)
        self.assertIn("data-copy", out)
        self.assertIn("https://example.com/issue", out)


if __name__ == "__main__":
    unittest.main()
