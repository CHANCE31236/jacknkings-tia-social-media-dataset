# Jacknkings & TIA Supermarché — Social Media Performance Dataset

Post-level and daily account-level social media data for two European retail brands — an Asian food brand and an Asian supermarket chain in France — covering **Instagram, Facebook, TikTok and YouTube**.

## What's in this dataset

- **165 posts** across 4 platforms with views, reach, engagement (likes / comments / shares / saves), follower growth, and watch time (on Meta platforms).
- **278 daily rows** of TikTok account-level metrics (video views, profile views, net likes, comments, shares) for both brands.
- **Content themes** (`Product` / `Store Opening` / `Brand`) labelled on Meta and TikTok posts.
- Coverage period: **15 April – 31 August 2026** — the first 5 months of a 6-month social media engagement.

## About the brands

- **Jacknkings** — an Asian prepared-food and seafood brand owned by **GGI**. On social media it currently promotes its signature fruit-shaped ice cream (trompe-l'œil ice creams).
- **TIA Supermarché** — an Asian supermarket brand owned by **SARL Legrand** (France), with stores in Tours, Reims, Orléans-Saran and Cormontreuil.

The author works in digital marketing at both companies. The dataset is shared publicly as a portfolio and open-data resource.

## Why this dataset is interesting

- Cross-platform content performance for the **same two brands** (Meta + TikTok + YouTube).
- Real-world, small-business social media data — useful for content-strategy analysis, engagement-rate benchmarking, and store-opening / new-product campaign analysis.
- Captions are reproduced **verbatim** (mostly French, with emoji), so the data also supports multilingual text analysis.

## Files

| File | Description |
|---|---|
| `social_media_posts.csv` | Post-level data — 165 rows, 4 platforms. |
| `tiktok_daily_account_metrics.csv` | TikTok daily account-level metrics — 278 rows. |

## Data dictionary — `social_media_posts.csv`

| Column | Type | Description |
|---|---|---|
| `post_id` | string | Unique identifier of the post. |
| `brand` | string | Brand name: `TIA` (TIA Supermarché) or `Jacknkings`. |
| `platform` | string | `Instagram`, `Facebook`, `TikTok` or `YouTube`. |
| `post_date` | string | Publication date, ISO format `YYYY-MM-DD`. |
| `content_theme` | string | Content theme: `Product`, `Store Opening` or `Brand` (empty for YouTube). |
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
| `likes` | integer | Net likes on that day (can be negative — likes/unlikes are netted). |
| `comments` | integer | Comments on that day. |
| `shares` | integer | Shares on that day. |

## Methodology & notes

- `spectators` (unique accounts that watched) was removed because it is redundant with `reach`.
- **Watch-time units were normalised to seconds** — Instagram exported durations (e.g. `5 h 3 min`) and Facebook exported milliseconds; both were converted to seconds.
- Two Instagram rows had watch data flagged "from ads" with an incomplete `watch_total`; their `watch_total` is left blank (their `watch_avg` is retained).
- **Platform coverage differs**: Meta exports rich engagement metrics (`reach`, `interactions`, `saves`, `followers_gain`, watch time, `crosspost`); TikTok and YouTube exports only provide `views`, `likes`, `comments` and `shares`, so the Meta-specific columns are empty for those platforms.
- `content_theme` is labelled for Meta and TikTok but not yet for YouTube.

## Source

Data was exported from the official back-ends of **Meta (Facebook & Instagram)**, **TikTok**, and **YouTube** for the brands' own accounts. Captions are reproduced verbatim from the published posts.

## License

**CC BY-NC 4.0** (Creative Commons Attribution-NonCommercial 4.0 International) — you must give appropriate credit and may not use the material for commercial purposes.

## Citation

If you use this dataset, please cite it by name: *Jacknkings & TIA Supermarché — Social Media Performance Dataset*, with a link to its source repository.
