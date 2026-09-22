# Jacknkings & TIA Supermarché — Social Media Performance Dataset

Post-level and daily account-level social media data for two European retail brands, exported from the official **Meta (Instagram & Facebook)**, **TikTok**, and **YouTube** back-ends.

## Overview

| | |
|---|---|
| **Brands** | Jacknkings, TIA Supermarché |
| **Platforms** | Instagram, Facebook, TikTok, YouTube |
| **Period** | 15 April – 31 August 2026 (first 5 months of a 6-month engagement) |
| **Posts** | 165 |
| **TikTok daily rows** | 278 |
| **License** | CC BY-NC 4.0 (Attribution-NonCommercial) |

## About the brands

- **Jacknkings** — an Asian prepared-food and seafood brand owned by **GGI**. On social media it currently promotes its signature fruit-shaped ice cream (trompe-l'œil ice creams).
- **TIA Supermarché** — an Asian supermarket brand owned by **SARL Legrand** (France), with stores in French cities such as Tours, Reims, Orléans-Saran and Cormontreuil.

The author works in digital marketing at both companies. The dataset covers the **first 5 months** of a 6-month reporting window (April–August 2026), shared publicly as a portfolio and open-data resource.

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
| `interactions` | integer | Total interactions = likes + comments + shares + saves (**Meta only**). |
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
| `likes` | integer | Net likes on that day (can be negative — unfollows/unlikes are netted). |
| `comments` | integer | Comments on that day. |
| `shares` | integer | Shares on that day. |

## Notes

- **`spectators`** (unique accounts that watched) was present in the raw Meta export and is **removed** from this dataset because it is redundant with `reach`.
- **Watch-time units were normalised to seconds**:
  - Instagram exported `watch_total` as a human-readable duration (e.g. `5 h 3 min`) → converted to seconds.
  - Facebook exported `watch_total` in **milliseconds** → converted to seconds (rounded).
  - `watch_avg` was already in seconds on both platforms (the `s` suffix and the note `à partir des publicités` / "from ads" were stripped).
- **Two Instagram rows** (`META_JNK_IG_2026-07-27_47`, `META_JNK_IG_2026-07-19_48`) had watch-time data flagged "from ads" with an incomplete `watch_total`; their `watch_total` is left **blank** (their `watch_avg` is retained).
- **Platform coverage differs**: Meta exports rich engagement metrics (`reach`, `interactions`, `saves`, `followers_gain`, watch time, `crosspost`); TikTok and YouTube exports only provide `views`, `likes`, `comments` and `shares`, so the Meta-specific columns are empty for those platforms.
- **`content_theme`** is labelled for Meta and TikTok but not yet for YouTube.

## Source & collection

- Data was exported from the official back-ends of **Meta (Facebook & Instagram)**, **TikTok**, and **YouTube** for the brands' own accounts.
- `caption` is reproduced verbatim from the published posts (original language, including emoji and hashtags).

## License

This dataset is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. You must give appropriate credit and may not use the material for commercial purposes. See `LICENSE`.

## Citation

If you use this dataset, please cite it with the repository name and a link to its source.
