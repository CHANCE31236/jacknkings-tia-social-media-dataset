"""Protect metric coverage and the integrity of the released CSV snapshot."""
import sys
import unittest
from pathlib import Path
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "analysis"))
from analyze_core import load_data, summarize


class AnalysisTests(unittest.TestCase):
    def test_interaction_rate_uses_matching_platform_coverage(self):
        posts = pd.DataFrame({
            "platform": ["Instagram", "Facebook", "TikTok"],
            "views": [100, 100, 800], "interactions": [10, 10, None],
            "reach": [50, 50, None], "followers_gain": [1, 1, None],
            "watch_total": [200, 200, None],
        })
        result = summarize(posts)
        self.assertEqual(result["total_views"], 1000)
        self.assertEqual(result["meta_interactions_per_view_pct"], 10)

    def test_rate_is_undefined_without_meta_views(self):
        posts = pd.DataFrame({
            "platform": ["TikTok"], "views": [0],
            "interactions": [None], "reach": [None],
            "followers_gain": [None], "watch_total": [None],
        })
        result = summarize(posts)
        self.assertIsNone(result["meta_interactions_per_view_pct"])
        self.assertIsNone(result["instagram_tiktok_view_share_pct"])

    def test_released_snapshot_has_unique_keys_and_documented_coverage(self):
        posts, daily = load_data()
        self.assertEqual(len(posts), 165)
        self.assertEqual(len(daily), 278)
        self.assertFalse(posts.post_id.duplicated().any())
        self.assertFalse(daily.duplicated(["brand", "date"]).any())
        self.assertEqual(set(posts.brand), {"TIA", "Jacknkings"})
        self.assertEqual(set(posts.platform), {"Instagram", "Facebook", "TikTok", "YouTube"})
        for frame, date in [(posts, "post_date"), (daily, "date")]:
            self.assertEqual(str(frame[date].min().date()), "2026-04-15")
            self.assertEqual(str(frame[date].max().date()), "2026-08-31")
        result = summarize(posts)
        self.assertEqual(result["total_views"], 460611)
        self.assertEqual(result["meta_views"], 359753)
        self.assertEqual(result["meta_interactions"], 15119)
        self.assertAlmostEqual(result["meta_interactions_per_view_pct"], 4.2026056767)


if __name__ == "__main__":
    unittest.main()
