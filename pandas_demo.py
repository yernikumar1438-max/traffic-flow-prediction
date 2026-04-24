# 🔹 1. Data Loading
import pandas as pd

# Fix: Create a sample DataFrame as 'data.csv' is not found.
data = {'marks': [60, 85, 45, 92, 70, 55, 78, 30],
        'department': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B'],
        'salary': [50000, 60000, 55000, 70000, 62000, 53000, 68000, 48000]}
df = pd.DataFrame(data)

# 🔹 2. Data Inspection
print("=== head() ===")
print(df.head())
print("\n=== tail() ===")
print(df.tail())
print("\n=== info() ===")
print(df.info())
print("\n=== describe() ===")
print(df.describe())

# 🔹 3. Data Cleaning
df = df.dropna()
df['marks'] = df['marks'].fillna(0)
df = df.rename(columns={'marks': 'student_marks'})

# 🔹 4. Data Selection & Filtering
print("\n=== loc[0] ===")
print(df.loc[0])
print("\n=== iloc[0] ===")
print(df.iloc[0])
filtered = df[df['student_marks'] > 50]
print("\n=== Filtered (student_marks > 50) ===")
print(filtered)

# 🔹 5. Data Manipulation
df['grade'] = ['Pass' if m > 50 else 'Fail' for m in df['student_marks']]
df['bonus'] = df['student_marks'] * 0.1
df = df.sort_values(by='student_marks', ascending=False)
print("\n=== After manipulation ===")
print(df)

# 🔹 6. Grouping & Aggregation
avg_salary = df.groupby('department')['salary'].mean()
print("\n=== Avg Salary by Department ===")
print(avg_salary)

# 🔹 7. Merging & Joining
df1 = pd.DataFrame({'id': [1, 2], 'name': ['A', 'B']})
df2 = pd.DataFrame({'id': [1, 2], 'score': [90, 80]})
merged = pd.merge(df1, df2, on='id')
concat_df = pd.concat([df1, df2], axis=1)
print("\n=== Merged DataFrame ===")
print(merged)
print("\n=== Concatenated DataFrame ===")
print(concat_df)

# 🔹 8. Data Transformation
df['student_marks'] = df['student_marks'].apply(lambda x: x + 5)
df['grade'] = df['grade'].map({'Pass': 'P', 'Fail': 'F'})
df['student_marks'] = df['student_marks'].astype(float)
print("\n=== After Transformation ===")
print(df)

# 🔹 9. Data Visualization
import matplotlib
matplotlib.use('Agg')   # Non-interactive backend so it works without a display
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of student_marks
plt.figure(figsize=(7, 4))
plt.hist(df['student_marks'], bins=6, color='steelblue', edgecolor='black')
plt.title('Distribution of Student Marks')
plt.xlabel('Student Marks')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('histogram_marks.png')
plt.close()
print("\n✅ Histogram saved as 'histogram_marks.png'")

# Boxplot of salary by department
plt.figure(figsize=(7, 4))
sns.boxplot(x='department', y='salary', data=df)
plt.title('Salary by Department')
plt.tight_layout()
plt.savefig('boxplot_salary.png')
plt.close()
print("✅ Boxplot saved as 'boxplot_salary.png'")

# 🔹 10. Exporting Data
df.to_csv("cleaned_data.csv", index=False)
df.to_excel("cleaned_data.xlsx", index=False)
print("\n✅ Data exported to 'cleaned_data.csv' and 'cleaned_data.xlsx'")
print("\n🎉 All steps completed successfully!")
