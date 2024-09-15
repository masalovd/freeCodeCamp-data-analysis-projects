import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    years_from_1880_to_2050 = np.arange(1880, 2051)
    years_from_2000_to_2050 = years_from_1880_to_2050[years_from_1880_to_2050 >= 2000]

    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df.loc[df['Year'] >= 2000, 'Year'], df.loc[df['Year'] >= 2000, 'CSIRO Adjusted Sea Level'])

    line1 = slope1 * years_from_1880_to_2050 + intercept1
    line2 = slope2 * years_from_2000_to_2050 + intercept2
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(15, 6))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, edgecolors='w', linewidth=0.5)
    
    # Create first line of best fit
    ax.plot(years_from_1880_to_2050, line1, color='red', label='Projected Sea Level based on CSIRO data (1880-2050)')

    # Create second line of best fit
    ax.plot(years_from_2000_to_2050, line2, color='green', label='Projected Sea Level based on CSIRO data (2000-2050)')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
