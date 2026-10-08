# Social Media Performance Analysis — Jacknkings & TIA Supermarché

**Period:** 15 April–31 August 2026 · **Posts:** 165 · **TikTok daily rows:** 278

**Source:** the two CSV files in `data/`. Totals below are computed from the committed snapshot.

## 1. Headline metrics

| Metric | Value |
|---|---:|
| All-platform post views | 460,611 |
| Meta post views (Instagram + Facebook) | 359,753 |
| Sum of Meta post reach | 144,794 |
| Meta platform-reported interactions | 15,119 |
| Meta net followers gained | 461 |
| Reported Meta watch time | 868,133 s (about 241 h) |
| Meta interactions per Meta view | 4.20% |

The interaction ratio is `15,119 / 359,753`. TikTok and YouTube lack the same aggregate interaction field, so their views are excluded from that denominator. The sum of post reach is not a deduplicated audience count. Missing watch-time cells are excluded from the reported sum.

## 2. Views by platform

| Platform | Posts | Views | Share |
|---|---:|---:|---:|
| Facebook | 54 | 221,527 | 48.1% |
| Instagram | 62 | 138,226 | 30.0% |
| TikTok | 17 | 78,829 | 17.1% |
| YouTube | 32 | 22,029 | 4.8% |

Facebook leads in observed post views. Its largest post contributes 91,566 views (41.3% of its platform total), making the aggregate sensitive to a single high-performing post.

## 3. Instagram + TikTok contribution

Instagram and TikTok together account for **217,055 views**, or **47.1%** of the post total. This measures platform share; the CSV lacks a content-format field that would identify every Instagram post as a Reel.

The separate TikTok account-level daily file totals **104,890 video views** and **2,659 profile views**. It has a different aggregation scope and should not be added to post-level views.

## 4. Content themes on Meta

| Theme | Posts | Views | Share of Meta views | Mean views per post |
|---|---:|---:|---:|---:|
| Brand | 42 | 170,175 | 47.3% | 4,052 |
| Product | 64 | 100,443 | 27.9% | 1,569 |
| Store Opening | 10 | 89,135 | 24.8% | 8,914 |

Brand posts constitute 36.2% of the **116 Meta posts**. Store Opening has the largest observed mean views per post. These descriptive differences depend on posting volume, timing, and individual outliers; they do not establish which content caused more conversions.

## 5. Highest-viewed posts

| Rank | Brand | Platform | Date | Theme | Views | Cross-post |
|---|---|---|---|---|---:|---|
| 1 | TIA | Facebook | 2026-04-30 | Brand | 91,566 | N |
| 2 | TIA | TikTok | 2026-04-27 | Brand | 31,689 | Unavailable |
| 3 | TIA | Instagram | 2026-04-30 | Store Opening | 31,341 | Y |
| 4 | TIA | Facebook | 2026-04-30 | Store Opening | 31,341 | Y |
| 5 | TIA | TikTok | 2026-06-22 | Store Opening | 20,157 | Unavailable |

Cross-post status identifies distribution across platforms. Promotion spend and paid/organic attribution are not available, so this field cannot substantiate an organic-only claim.

## 6. Monthly totals

| Month | Posts | All-platform views | Meta interactions |
|---|---:|---:|---:|
| April 2026 | 28 | 199,056 | 2,971 |
| May 2026 | 28 | 67,249 | 976 |
| June 2026 | 59 | 95,192 | 1,226 |
| July 2026 | 30 | 76,425 | 9,730 |
| August 2026 | 20 | 22,689 | 216 |

April starts on the 15th, so monthly coverage is unequal. July has the largest exported interaction total. The aggregate interaction field differs from `likes + comments + shares + saves` in 106 of 116 Meta rows; original platform definitions should be checked before attributing this pattern to an engagement mechanism.

## 7. Interpretation and follow-up

- Facebook supplies 48.1% of observed post views, with substantial concentration in its largest post.
- Instagram + TikTok supply 47.1% of views; daily account metrics describe a separate scope.
- Compare theme medians and outlier sensitivity before using theme means to make content decisions.
- Add documented promotion attribution, export timestamps, and conversion metrics to support stronger performance conclusions.

Cross-platform view definitions can differ. Repeated viewers and cross-posted content are not deduplicated, and this snapshot describes observed exports rather than a controlled comparison.

## Reproducibility

Use Python 3.10 or newer and run from the repository root:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python analysis/analyze_core.py
python analysis/gen_charts.py
```

The scripts resolve input paths relative to the repository and also run from another working directory. `gen_charts.py` creates six PNG charts in `analysis/`: platform totals, monthly totals, theme metrics (all in thousands), ten separately positioned top posts, TikTok daily views, and Instagram + TikTok platform share. Generated charts are excluded from Git. Data dictionaries are in `README.md`.
