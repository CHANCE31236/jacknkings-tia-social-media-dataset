"""Compute descriptive KPIs from the committed social media exports."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
META_PLATFORMS = ("Instagram", "Facebook")


def load_data(root=ROOT):
    """Locate exports relative to the script, independently of the caller."""
    root = Path(root)
    posts = pd.read_csv(root / "data" / "social_media_posts.csv")
    daily = pd.read_csv(root / "data" / "tiktok_daily_account_metrics.csv")
    posts["post_date"] = pd.to_datetime(posts["post_date"], errors="raise")
    daily["date"] = pd.to_datetime(daily["date"], errors="raise")
    return posts, daily


def summarize(posts):
    """Keep platform-reported Meta interactions paired with Meta views."""
    meta = posts[posts.platform.isin(META_PLATFORMS)]
    total_views = int(posts.views.sum())
    meta_views = int(meta.views.sum())
    interactions = int(meta.interactions.sum())
    combined_views = int(posts[posts.platform.isin(("Instagram", "TikTok"))].views.sum())
    return {
        "total_views": total_views,
        "meta_views": meta_views,
        "meta_reach_sum": int(meta.reach.sum()),
        "meta_interactions": interactions,
        "meta_followers_gain": int(meta.followers_gain.sum()),
        "meta_watch_seconds": int(meta.watch_total.sum()),
        "meta_interactions_per_view_pct": interactions / meta_views * 100 if meta_views else None,
        "instagram_tiktok_views": combined_views,
        "instagram_tiktok_view_share_pct": combined_views / total_views * 100 if total_views else None,
    }


def main():
    posts, daily = load_data()
    for key, value in summarize(posts).items():
        print(f"{key}: {round(value, 2) if isinstance(value, float) else value}")
    print()
    platforms = posts.groupby("platform").agg(
        posts=("post_id", "count"), views=("views", "sum")
    ).sort_values("views", ascending=False)
    platforms["share_pct"] = (platforms.views / platforms.views.sum() * 100).round(1)
    print(platforms)
    print()
    meta = posts[posts.platform.isin(META_PLATFORMS)]
    print(meta.groupby("content_theme").agg(
        posts=("post_id", "count"), views=("views", "sum")
    ).sort_values("views", ascending=False))
    print()
    print("TikTok daily video views:", int(daily.video_views.sum()))
    print("TikTok daily profile views:", int(daily.profile_views.sum()))


if __name__ == "__main__":
    main()
