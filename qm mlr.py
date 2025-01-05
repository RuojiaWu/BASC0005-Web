import pandas as pd
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

# Load the data
unemployment = pd.read_excel("/Users/casey/Desktop/unemployment.xlsx")
education = pd.read_excel("/Users/casey/Desktop/Education.xlsx")
income = pd.read_excel("/Users/casey/Desktop/income.xlsx")
depression = pd.read_excel("/Users/casey/Desktop/depression.xlsx")
poverty = pd.read_csv("/Users/casey/Desktop/poverty.csv")

# Standardize column names for consistency
poverty.rename(columns={'Name': 'State'}, inplace=True)
unemployment.rename(columns={'state': 'State'}, inplace=True)
income.rename(columns={'state': 'State'}, inplace=True)
education.rename(columns={'state': 'State'}, inplace=True)
depression.rename(columns={'LocationDesc': 'State', 'Data_Value': 'depression'}, inplace=True)

# Merge datasets on 'State'
merged_data = pd.merge(unemployment[['State', 'unemployment']],
                       education[['State', 'Average Growth in Awarded Degrees']], 
                       on='State', how='inner')
merged_data = pd.merge(merged_data, income[['State', 'Median Household Income']], on='State', how='inner')
merged_data = pd.merge(merged_data, poverty[['State', 'Percent in Poverty']], on='State', how='inner')
merged_data = pd.merge(merged_data, depression[['State', 'depression']], on='State', how='inner')


# Handle missing values
merged_data.dropna(inplace=True)

# Define independent variables
X = merged_data[['unemployment', 'Average Growth in Awarded Degrees', 
                 'Median Household Income', 'Percent in Poverty']]

# Standardize independent variables
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert scaled data back to DataFrame
X_scaled = pd.DataFrame(X_scaled, columns=X.columns)

# Add constant for OLS
X_scaled = sm.add_constant(X_scaled)

# Define dependent variable
y = merged_data['depression']

# Fit OLS model
model = sm.OLS(y, X_scaled)
results = model.fit()

# Display regression summary
print(results.summary())
