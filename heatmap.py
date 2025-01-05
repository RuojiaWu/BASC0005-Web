

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('/Users/helen/BASc/BASc0005/project/merged_data by state final .csv')  
df['Median Household Income (USD)'] = df['Median Household Income (USD)'].str.replace(',', '').astype(float)
# Filter data by year and calculate statistics
years = [2020, 2021, 2022]
stats = []

for year in years:
    filtered_df = df[df['Year'] == year]  # Filter rows for 2020-2022
    stats.append({
        'Year': year,
        'Mean_Avg_Growth_Degrees': filtered_df['Average Growth in Awarded Degrees'].mean(),
        'Mean_Unemployment_Rate': filtered_df['Unemployment_Rate'].mean(),
        'Mean_Percent_in_Poverty': filtered_df['Percentage in Poverty'].mean(),
        'Median_Household_Income': filtered_df['Median Household Income (USD)'].median()
    })

# Create a DataFrame for calculated statistics
stats_df = pd.DataFrame(stats)
print(stats_df)

# Draw a heatmap for correlations of the filtered data
def draw_corr_picture(data):
    corrmat = data.corr()  # Calculate correlation matrix
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None) 
    pd.set_option('display.width', None) 
    pd.set_option('display.max_colwidth', None)
    print("correlation matrix:\n", corrmat)
    plt.subplots(figsize=(12, 12))  # Set figure size
    sns.heatmap(corrmat, vmax=0.9, square=True, cmap='Blues', annot=False)  # Draw heatmap
    plt.show()

#Ouput the heatmap
heatmap_data = df[['Average Growth in Awarded Degrees', 'Unemployment_Rate', 'Percentage in Poverty', 'Median Household Income (USD)']]
draw_corr_picture(heatmap_data)

