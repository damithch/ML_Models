import pdfplumber
import pandas as pd
import matplotlib.pyplot as plt

# Use raw string to avoid unicode escape errors
pdf_path = r"C:\Users\starg\Downloads\Malabe - Regular - CA Overall_3c3e59bbb504a8f9d4ce8bdb6f46bcf0.pdf"

# Open the PDF
with pdfplumber.open(pdf_path) as pdf:
    # Extract table from the first page
    page = pdf.pages[0]
    table = page.extract_table()

# If a table was extracted, proceed with analysis
if table:
    # Convert the extracted table into a Pandas DataFrame
    df = pd.DataFrame(table[1:], columns=table[0])  # First row as column headers

    # Data Cleaning: Convert columns to appropriate data types
    # Let's assume that 'Feature_1', 'Feature_2' and 'Target' are numeric columns
    df['Feature_1'] = pd.to_numeric(df['Feature_1'], errors='coerce')  # Convert to numeric, handle errors
    df['Feature_2'] = pd.to_numeric(df['Feature_2'], errors='coerce')
    df['Target'] = pd.to_numeric(df['Target'], errors='coerce')

    # Print the first few rows of the DataFrame
    print("Cleaned Data:")
    print(df.head())

    # Handle missing data: Fill missing values with mean or drop rows
    df = df.fillna(df.mean())  # Fill NaN with mean values (you can also choose to drop NaNs)

    # Summary statistics of the numeric columns
    print("\nSummary Statistics:")
    print(df.describe())

    # Data Visualization

    # 1. Histogram of 'Feature_1'
    plt.figure(figsize=(10, 6))
    plt.hist(df['Feature_1'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Histogram of Feature 1')
    plt.xlabel('Feature 1')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

    # 2. Scatter plot between 'Feature_1' and 'Feature_2'
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Feature_1'], df['Feature_2'], c=df['Target'], cmap='coolwarm', edgecolor='k', alpha=0.7)
    plt.title('Scatter Plot between Feature 1 and Feature 2')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.colorbar(label='Target')
    plt.grid(True)
    plt.show()

    # 3. Correlation Matrix (if the columns are numeric)
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    # Heatmap of the correlation matrix
    import seaborn as sns

    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix Heatmap')
    plt.show()

else:
    print("No table found on the page.")
