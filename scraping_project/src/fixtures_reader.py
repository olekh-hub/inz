import pandas as pd

df = pd.read_csv('fixtures.csv')
df_selected = df[['Date', 'Home', 'Away']]

df_2 = pd.read_csv('match_data.csv')
map_teams = dict(zip(sorted(df_selected['Home']), sorted(df_2['home_team'])))

df_selected['Home'] = df_selected['Home'].map(map_teams)
df_selected['Away'] = df_selected['Away'].map(map_teams)


df_selected['match_key'] = df_selected['Home'] + '-' + df_selected['Away']
df_2['match_key'] = df_2['home_team'] + '-' + df_2['away_team']

res = pd.merge(df_selected, df_2, on='match_key', how='inner')
print(f'Rows in df: {df.shape[0]}')
print(f'Rows in df_2: {df_2.shape[0]}')
print(res.columns)
res = res[['Date', 'Home', 'Away', 'match_id']]
res.to_csv('matches_data.csv', index=False)