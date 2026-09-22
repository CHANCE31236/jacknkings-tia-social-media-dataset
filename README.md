# Jacknkings & TIA Supermarché — Social Media Post Performance

A post-level dataset of social media content and engagement metrics for two European retail brands, exported from the official Meta (Instagram & Facebook) back-end.

## Overview

| | |
|---|---|
| **Brands** | Jacknkings, TIA Supermarché |
| **Platforms** | Instagram, Facebook |
| **Period** | 15 April – 31 August 2026 (first 5 months of a 6-month engagement) |
| **Posts** | 116 |
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
    └── social_media_posts.csv   # the dataset
```

## Data dictionary

| Column | Type | Description |
|---|---|---|
| `post_id` | string | Unique identifier of the post (`META_<brand>_<platform>_<date>_<n>`). |
| `brand` | string | Brand name: `TIA` (TIA Supermarché) or `Jacknkings`. |
| `platform` | string | `Instagram` or `Facebook`. |
| `post_date` | string | Publication date, format `YYYY/M/D`. |
| `crosspost` | string | Whether the post was cross-posted between platforms: `Y` = yes, `N` = no. |
| `caption` | string | Original post caption, kept as published (mostly French, may include emoji). |
| `views` | integer | Total number of video/post views. |
| `reach` | integer | Number of unique accounts that saw the post. |
| `interactions` | integer | Total interactions (sum of likes, comments, shares and saves). |
| `likes` | integer | Number of likes. |
| `comments` | integer | Number of comments. |
| `shares` | integer | Number of shares. |
| `saves` | integer | Number of saves/bookmarks. |
| `followers_gain` | integer | Net new followers attributed to the post. |
| `watch_total` | integer | **Total watch time in seconds** (sum across all viewers). |
| `watch_avg` | integer | **Average watch time in seconds** (per viewer). |

### Notes

- **`spectators`** (unique accounts that watched) was present in the raw export and is **removed** from this dataset because it is redundant with `reach`.
- **Watch-time units were normalised to seconds**:
  - Instagram exported `watch_total` as a human-readable duration (e.g. `5 h 3 min`) → converted to seconds.
  - Facebook exported `watch_total` in **milliseconds** → converted to seconds (rounded).
  - `watch_avg` was already in seconds on both platforms (the `s` suffix and the note `à partir des publicités` / "from ads" were stripped).
- **Two Instagram rows** (`META_JNK_IG_2026-07-27_47`, `META_JNK_IG_2026-07-19_48`) had watch-time data flagged "from ads" with an incomplete `watch_total`; their `watch_total` is left **blank** (their `watch_avg` is retained).

## Source & collection

- The data was exported from the **Meta (Facebook & Instagram) back-end** for the brands' own accounts.
- `caption` is reproduced verbatim from the published posts (original language, including emoji and hashtags).

## License

This dataset is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license. You must give appropriate credit and may not use the material for commercial purposes. See `LICENSE`.

## Citation

If you use this dataset, please cite it with the repository name and a link to its source.
