# Jacknkings & TIA Supermarché — Social Media Performance Dataset

Post-level and daily account-level social media data for two European retail brands, exported from the official **Meta (Instagram & Facebook)**, **TikTok**, and **YouTube** back-ends.

## Overview

| | |
|---|---|
| **Brands** | Jacknkings, TIA Supermarché |
| **Platforms** | Instagram, Facebook, TikTok, YouTube |
| **Period** | 15 April – 31 August 2026 (five calendar months, with partial April coverage) |
| **Posts** | 165 |
| **TikTok daily rows** | 278 |
| **License** | CC BY-NC 4.0 (Attribution-NonCommercial) |

## About the brands

- **Jacknkings** — an Asian prepared-food and seafood brand owned by **GGI**. On social media it currently promotes its signature fruit-shaped ice cream (trompe-l'œil ice creams).
- **TIA Supermarché** — an Asian supermarket brand owned by **SARL Legrand** (France), with stores in French cities such as Tours, Reims and Orléans-Saran.

The author works in digital marketing at both companies. The dataset covers **five calendar months** (15 April–31 August 2026, including partial April coverage), shared publicly as a portfolio and open-data resource.

## Files

```
├── README.md
├── LICENSE
└── data/
    ├── social_media_posts.csv              # post-level, all 4 platforms (165 rows)
    └── tiktok_daily_account_metrics.csv    # TikTok daily account-level (278 rows)
```

## Data dictionary — `social_media_posts.csv`

| Column | Type | Description |
|---|---|---|
| `post_id` | string | Unique identifier of the post. |
| `brand` | string | Brand name: `TIA` (TIA Supermarché) or `Jacknkings`. |
| `platform` | string | `Instagram`, `Facebook`, `TikTok` or `YouTube`. |
| `post_date` | string | Publication date, ISO format `YYYY-MM-DD`. |
| `content_theme` | string | Content theme: `Product`, `Store Opening` or `Brand` (empty for YouTube, which is unlabelled). |
| `caption` | string | Original post caption / video title, kept as published (mostly French, may include emoji and hashtags). |
| `views` | integer | Total number of video/post views. |
| `reach` | integer | Number of unique accounts that saw the post (**Meta only**). |
| `interactions` | integer | Platform-reported aggregate interactions (**Meta only**); retained as exported. It differs from the sum of the four listed component columns in 106 of 116 Meta rows. |
| `likes` | integer | Number of likes. |
| `comments` | integer | Number of comments. |
| `shares` | integer | Number of shares. |
| `saves` | integer | Number of saves/bookmarks (**Meta only**). |
| `followers_gain` | integer | Net new followers attributed to the post (**Meta only**). |
| `watch_total` | integer | **Total watch time in seconds** (sum across all viewers; **Meta only**). |
| `watch_avg` | integer | **Average watch time in seconds** (per viewer; **Meta only**). |
| `crosspost` | string | Whether the post was cross-posted between platforms: `Y` = yes, `N` = no (**Meta only**). |

## Data dictionary — `tiktok_daily_account_metrics.csv`

| Column | Type | Description |
|---|---|---|
| `brand` | string | `TIA` or `Jacknkings`. |
| `date` | string | Date, ISO format `YYYY-MM-DD`. |
| `video_views` | integer | Total video views on that day. |
| `profile_views` | integer | Total profile views on that day. |
| `likes` | integer | Net likes on that day (can be negative when likes are removed). |
| `comments` | integer | Comments on that day. |
| `shares` | integer | Shares on that day. |

## Notes

- **Watch-time metrics** (watch_total and watch_avg) have been standardized to seconds across all platforms.
- **Two Instagram rows** (`META_JNK_IG_2026-07-27_47`, `META_JNK_IG_2026-07-19_48`) had watch-time data flagged "from ads" with an incomplete `watch_total`; their `watch_total` is left **blank** (their `watch_avg` is retained).

## Reproduce the analysis

Use Python 3.10 or newer. From the repository root:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS / Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python analysis/analyze_core.py
python analysis/gen_charts.py
```

Both scripts locate `data/` relative to their own location, so they also run from another working directory. Charts are written to `analysis/`. See [the analysis report](analysis/ANALYSIS.md) for computed totals and interpretation limits. GitHub Actions runs the tests and both scripts on every pull request.

## Metric interpretation

- Empty numeric cells mean unavailable metrics and are distinct from measured zeroes.
- `interactions` is retained as reported by Meta. The export does not explain its differences from the component sum; check the original reporting definitions before deriving component-based rates.
- Meta interactions per view use only Instagram and Facebook views as the denominator. TikTok and YouTube do not supply the same aggregate interaction field.
- Summing post-level reach does not produce a deduplicated audience count. Cross-posted content and repeated viewers can contribute to several rows.
- The exports do not include promotion spend, conversion outcomes, or a per-post content-format field. Cross-post status describes distribution and does not establish whether a post was promoted.

## License

This dataset is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. You must give appropriate credit and may not use the material for commercial purposes. See `LICENSE`.

## Citation

If you use this dataset, please cite it with the repository name and a link to its source.
