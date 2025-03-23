import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
file_path = "sample_data.csv"  # Replace with actual dataset file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    data = {"Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
            "Age": [25, 30, 35, None, 40],
            "Salary": [50000, 60000, 70000, 80000, None],
            "Department": ["HR", "IT", "Finance", "IT", "HR"]}
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print("Sample dataset created as 'sample_data.csv'")

# Display first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# Data Cleaning
print("\nHandling missing values...")
df.fillna(df.mean(numeric_only=True), inplace=True)
print(df)

# Data Exploration
print("\nSummary statistics:")
print(df.describe())

# Filtering data
filtered_df = df[df["Age"] > 30]
print("\nFiltered data (Age > 30):")
print(filtered_df)

# Sorting data
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted data (by Salary descending):")
print(sorted_df)

# Data Visualization
plt.figure(figsize=(8, 5))
df["Age"].hist(bins=5, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.grid(False)
plt.show()

plt.figure(figsize=(8, 5))
df.plot(kind="bar", x="Name", y="Salary", color="orange")
plt.title("Salary Comparison")
plt.ylabel("Salary")
plt.grid(False)
plt.show()

print("\nMini project completed! Upload the dataset and script to GitHub.")
