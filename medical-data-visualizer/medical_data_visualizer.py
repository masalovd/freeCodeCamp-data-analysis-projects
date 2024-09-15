import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('./medical_examination.csv')
df['age'] = (df['age'] / 365).astype(np.int32)

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')


    # 7
    custom_color_palette = ['#BD2D87', '#06BA63']
    catpl = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar', palette=custom_color_palette)


    # 8
    fig = catpl.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    correct_height = (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975))
    correct_weight = (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))
    df_heat = df[correct_height & correct_weight]

    # 12
    corr = df_heat.corr()

    # 13
    mask = mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(14,9))

    # 15
    sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".1f", linewidths=0.5, ax=ax)

    # 16
    fig.savefig('heatmap.png')
    return fig