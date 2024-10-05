#3. Using the sales data, generate a heatmap to visualize the variation in sales across different months and
#   days.

"""
np.random.seed(20)
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df = pd.DataFrame(data)
"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(20)

# Generate random sales data
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df = pd.DataFrame(data)

# Pivot the data to create a matrix for the heatmap
heatmap_data = df.pivot_table(values='Sales', index='Day', columns='Month', aggfunc='sum', fill_value=0)

# Create a heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=True, fmt='d')

# Add title and labels
plt.title('Sales Heatmap: Variation Across Months and Days')
plt.xlabel('Month')
plt.ylabel('Day')

# Show the plot
plt.show()

