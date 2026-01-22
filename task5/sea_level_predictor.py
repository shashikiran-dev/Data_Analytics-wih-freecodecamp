import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # 1. Import the data
    df = pd.read_csv("epa-sea-level.csv")

    # 2. Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Line of best fit using all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred_all = res_all.slope * years_extended + res_all.intercept

    plt.plot(years_extended, sea_level_pred_all, color='red')

    # 4. Line of best fit using data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(
        df_recent['Year'],
        df_recent['CSIRO Adjusted Sea Level']
    )

    years_recent = pd.Series(range(2000, 2051))
    sea_level_pred_recent = res_recent.slope * years_recent + res_recent.intercept

    plt.plot(years_recent, sea_level_pred_recent, color='green')

    # 5. Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Do not modify the next two lines
    plt.savefig('sea_level_plot.png')
    return plt.gca()
