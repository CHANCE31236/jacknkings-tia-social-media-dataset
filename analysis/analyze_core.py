# -*- coding: utf-8 -*-
"""KPI core analysis for jacknkings-tia dataset."""
import pandas as pd, numpy as np, os

D = '.'
p = pd.read_csv(os.path.join(D, 'data', 'social_media_posts.csv'))
t = pd.read_csv(os.path.join(D, 'data', 'tiktok_daily_account_metrics.csv'))
p['post_date'] = pd.to_datetime(p['post_date']); t['date'] = pd.to_datetime(t['date'])

print('total views:', int(p.views.sum()))
print('total reach:', int(p.reach.sum()))
print('total interactions:', int(p.interactions.sum()))
print('followers_gain:', int(p.followers_gain.sum()))
print('watch sec:', int(p.watch_total.sum()))
print('interaction rate %:', round(p.interactions.sum()/p.views.sum()*100,2))
print()
g = p.groupby('platform').agg(posts=('post_id','count'), views=('views','sum')).sort_values('views',ascending=False)
g['share'] = (g['views']/g['views'].sum()*100).round(1)
print(g)
print()
meta = p[p.platform.isin(['Instagram','Facebook'])]
print(meta.groupby('content_theme').agg(posts=('post_id','count'), views=('views','sum')).sort_values('views',ascending=False))
print()
# short-form share (post-level)
short = int(p[p.platform.isin(['Instagram','TikTok'])].views.sum())
print('short-form (IG+TikTok) views:', short, '=', round(short/p.views.sum()*100,1), '% of total')
