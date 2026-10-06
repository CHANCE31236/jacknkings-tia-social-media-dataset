# -*- coding: utf-8 -*-
"""Reproduce all charts in the ANALYSIS report."""
import pandas as pd, numpy as np, os
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = 'data'          # run from repo root
OUT = 'analysis'
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({'font.size': 11, 'axes.titlesize': 13, 'axes.titleweight': 'bold',
                     'figure.dpi': 130, 'axes.grid': True, 'grid.alpha': 0.25,
                     'axes.axisbelow': True, 'figure.facecolor': 'white'})
CMAP = ['#2f5e8e', '#e07b39', '#4a9d6f', '#9b5ea8', '#c75d5d', '#7f8fa6']

p = pd.read_csv(os.path.join(D, 'social_media_posts.csv'))
t = pd.read_csv(os.path.join(D, 'tiktok_daily_account_metrics.csv'))
p['post_date'] = pd.to_datetime(p['post_date']); t['date'] = pd.to_datetime(t['date'])

def save(fig, name):
    fig.tight_layout(); fig.savefig(os.path.join(OUT, name), bbox_inches='tight')
    plt.close(fig); print('saved', name)

# 1 views by platform
gp = p.groupby('platform').views.sum().sort_values(ascending=False)
fig, ax = plt.subplots(figsize=(6.5, 3.6))
bars = ax.bar(gp.index, gp.values, color=CMAP[:len(gp)])
for b, v in zip(bars, gp.values):
    ax.text(b.get_x()+b.get_width()/2, v, f'{v/1000:.1f}K\n({v/gp.sum()*100:.0f}%)', ha='center', va='bottom', fontsize=9)
ax.set_title('Post-level views by platform (Apr-Aug 2026)'); ax.set_ylabel('Views'); ax.set_ylim(0, gp.max()*1.15)
save(fig, 'fig1_views_by_platform.png')

# 2 monthly trend
p['month'] = p.post_date.dt.to_period('M').astype(str)
gm = p.groupby('month').agg(views=('views','sum'), interactions=('interactions','sum')).reindex(['2026-04','2026-05','2026-06','2026-07','2026-08'])
fig, ax = plt.subplots(figsize=(6.5, 3.6))
ax.bar(gm.index, gm.views, color=CMAP[0], label='Views')
ax2 = ax.twinx(); ax2.plot(gm.index, gm.interactions, color=CMAP[1], marker='o', linewidth=2, label='Interactions')
for i, v in enumerate(gm.views): ax.text(i, v, f'{v/1000:.0f}K', ha='center', va='bottom', fontsize=9)
ax.set_title('Monthly post views & interactions'); ax.set_ylabel('Views'); ax2.set_ylabel('Interactions'); ax.set_ylim(0, gm.views.max()*1.15)
ax.legend(loc='upper left'); ax2.legend(loc='upper right')
save(fig, 'fig2_monthly_trend.png')

# 3 theme (Meta)
meta = p[p.platform.isin(['Instagram','Facebook'])]
gth = meta.groupby('content_theme').agg(views=('views','sum'), reach=('reach','sum'), interactions=('interactions','sum')).reindex(['Brand','Product','Store Opening'])
fig, ax = plt.subplots(figsize=(6.5, 3.6))
x = np.arange(len(gth)); w = 0.27
ax.bar(x-w, gth.views/1000, w, color=CMAP[0], label='Views (K)')
ax.bar(x, gth.reach/1000, w, color=CMAP[2], label='Reach (K)')
ax.bar(x+w, gth.interactions, w, color=CMAP[1], label='Interactions')
ax.set_xticks(x); ax.set_xticklabels(gth.index)
ax.set_title('Content theme performance (Meta: IG + FB)'); ax.set_ylabel('K'); ax.legend()
save(fig, 'fig3_theme_performance.png')

# 4 top posts
tp = p.nlargest(10, 'views')
labels = [f"{r.platform}\n{r.brand[:6]}" for r in tp.itertuples()]
fig, ax = plt.subplots(figsize=(6.5, 4.0))
ax.barh(labels[::-1], tp.views.values[::-1], color=CMAP)
for i, v in enumerate(tp.views.values[::-1]): ax.text(v, i, f'{v/1000:.1f}K', va='center', fontsize=9)
ax.set_title('Top 10 posts by views'); ax.set_xlabel('Views'); ax.invert_yaxis()
save(fig, 'fig4_top_posts.png')

# 5 TikTok daily
fig, ax = plt.subplots(figsize=(6.5, 3.6))
for i, b in enumerate(t.brand.unique()):
    sub = t[t.brand==b].sort_values('date')
    ax.plot(sub.date, sub.video_views, marker='.', ms=3, lw=1.5, color=CMAP[i], label=b)
ax.set_title('TikTok daily video views by brand'); ax.set_ylabel('Video views'); ax.legend()
save(fig, 'fig5_tiktok_daily.png')

# 6 short-form share (post-level, consistent)
ig_views = int(p[p.platform=='Instagram'].views.sum())
tt_views = int(p[p.platform=='TikTok'].views.sum())
fb_views = int(p[p.platform=='Facebook'].views.sum())
yt_views = int(p[p.platform=='YouTube'].views.sum())
tot = ig_views+tt_views+fb_views+yt_views; short = ig_views+tt_views
fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.pie([short, fb_views, yt_views], labels=['Short-form\n(IG Reels + TikTok)','Facebook','YouTube'],
       autopct=lambda x: f'{x:.0f}%', colors=[CMAP[1], CMAP[0], CMAP[4]], startangle=90, explode=(0.03,0,0), textprops={'fontsize':10})
ax.set_title(f'Short-form (IG Reels + TikTok) = {short/tot*100:.0f}% of views\n({short/1000:.0f}K of {tot/1000:.0f}K, post-level)')
save(fig, 'fig6_short_video_share.png')
print('DONE')
