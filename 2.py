#2. Using the Student Grades, create a violin plot to display the distribution of scores across different grade
#   categories.
"""
np.random.seed(30)
data = {
    'X': np.random.uniform(-10, 10, 300),
    'Y': np.random.uniform(-10, 10, 300),
    'Z': np.random.uniform(-10, 10, 300)
}
df = pd.DataFrame(data)
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(30)

# Generate random scores
scores = np.random.uniform(0, 100, 300)

# Create grade categories based on scores
grade_categories = pd.cut(scores, bins=[0, 60, 70, 80, 90, 100], 
                          labels=['F', 'C', 'B', 'A', 'A+'])

# Create a DataFrame
df = pd.DataFrame({'Scores': scores, 'Grade': grade_categories})

# Create a violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='Grade', y='Scores', data=df, inner='quartile')

# Add title and labels
plt.title('Distribution of Scores Across Different Grade Categories')
plt.xlabel('Grade Categories')
plt.ylabel('Scores')

# Show the plot
plt.show()
