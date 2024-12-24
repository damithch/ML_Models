import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Use a non-GUI backend to avoid Tkinter issues
matplotlib.use('Agg')

# Set random seed for reproducibility
np.random.seed(42)

# Generate random data
num_samples = 500  # You can change this to generate more or fewer samples
feature_1 = np.random.normal(50, 10, num_samples)  # Normally distributed around 50
feature_2 = np.random.uniform(20, 80, num_samples)  # Uniform distribution between 20 and 80
target = np.random.choice([0, 1], size=num_samples)  # Random binary labels (0 or 1)

# Create a DataFrame
df = pd.DataFrame({
    'Feature_1': feature_1,
    'Feature_2': feature_2,
    'Target': target
})

# Display the first few rows in the console
print("Generated Random Data:")
print(df.head())

# Save the dataset to a CSV file
csv_filename = 'random_dataset.csv'
df.to_csv(csv_filename, index=False)
print(f"\nRandom dataset saved as '{csv_filename}'")

# Plot the data and save it as an image
plt.figure(figsize=(8, 6))
plt.scatter(df['Feature_1'], df['Feature_2'], c=df['Target'], cmap='coolwarm', edgecolor='k', alpha=0.7)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Random Data Scatter Plot (Colored by Target)')
plt.colorbar(label='Target')
plt.grid(True)

# Save the plot to an image file
plot_filename = 'scatter_plot.png'
plt.savefig(plot_filename)
print(f"Plot saved as '{plot_filename}'")
