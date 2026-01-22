import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# 1. Import the data
df = pd.read_csv("medical_examination.csv")

# 2. Add an overweight column
# BMI = weight (kg) / (height (m))^2
df['overweight'] = (
    df['weight'] / ((df['height'] / 100) ** 2) > 25
).astype(int)

# 3. Normalize cholesterol and glucose
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


def draw_cat_plot():
    # 4. Create DataFrame for cat plot using pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 5. Group and reformat the data
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    # 6. Draw the catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig

    # 7. Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 8. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 9. Calculate the correlation matrix
    corr = df_heat.corr()

    # 10. Generate a mask for the upper triangle
    mask = np.triu(corr)

    # 11. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 12. Plot the correlation matrix
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=0.5,
        cbar_kws={'shrink': 0.5}
    )

    # 13. Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
