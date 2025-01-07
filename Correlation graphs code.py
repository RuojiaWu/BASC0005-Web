import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to create a scatter plot with regression line
def create_scatter_plot(data, x_col, y_col):
    correlation = data[x_col].corr(data[y_col])
    r_squared = correlation ** 2
    
    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=data,
        x=x_col,
        y=y_col,
        scatter_kws={'s': 50, 'color': 'blue', 'alpha': 0.7},
        line_kws={'color': 'red', 'linewidth': 2}
    )
    plt.title(f'Scatter Plot of {x_col} vs {y_col}\nCorrelation Coefficient: {correlation:.2f}, R²: {r_squared:.2f}', fontsize=14)
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.grid(alpha=0.3)
    plt.show()

# Main function to upload CSV and create scatter plot
def main():
    file_path = input("Enter the path to your CSV file: ")
    try:
        data = pd.read_csv(file_path)
  
        print("Columns in the dataset:", list(data.columns))
        
        # User selects columns for x and y
        x_col = input("Enter the column name for the X-axis: ")
        y_col = input("Enter the column name for the Y-axis: ")
        
        if x_col in data.columns and y_col in data.columns:
            create_scatter_plot(data, x_col, y_col)
        else:
            print("Error: Column names do not exist in the dataset.")
    except Exception as e:
        print(f"Error: {e}")

# Run the main function
main()


