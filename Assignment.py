import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
df = pd.read_csv('/content/Salaries.csv')
df.head()
df.columns


# 1-Basic Data Exploration: Identify the number of rows and columns in the dataset
num_of_rows, num_of_columns = df.shape
print(f"Number of rows: {num_of_rows}")
print(f"Number of columns: {num_of_columns}")

# determine the data types of each column
data_types = df.dtypes
print("\nData types of each column:")
print(data_types)

#and check for missing values in each column.
missing_values = df.isnull().sum()
print("\nMissing values in each column:")
print(missing_values)


# 2-Descriptive Statistics: Calculate basic statistics mean, median, mode, minimum, and maximum salary, determine the range of salaries, and find the standard deviation.
mean_salary = df['TotalPay'].mean()
median_salary = df['TotalPay'].median()
mode_salary = df['TotalPay'].mode().iloc[0]
min_salary = df['TotalPay'].min()
max_salary = df['TotalPay'].max()
salary_range = max_salary - min_salary
std_dev_salary = df['TotalPay'].std()

print(f"Mean Salary: {mean_salary:.2f}")
print(f"Median Salary: {median_salary:.2f}")
print(f"Mode Salary: {mode_salary:.2f}")
print(f"Minimum Salary: {min_salary:.2f}")
print(f"Maximum Salary: {max_salary:.2f}")
print(f"Salary Range: {salary_range:.2f}")
print(f"Standard Deviation of Salary: {std_dev_salary:.2f}")


# 3-Data Cleaning: Handle missing data by suitable method with explain why you use it.
df_handeled = df.fillna(0)
df_handeled = df_handeled.drop(['Notes', 'Status'], axis=1)

# I used the fillna(0) function for 2 reasons:
#     1- if i chose to drop the missing data then we would be left with empty rows but we droped 'Notes' and 'Status' columns due to their limited contribution.
#     2- I chose a number to not changing the data types of the columns


# 4-Basic Data Visualization: Create histograms or bar charts to visualize the distribution of salaries, and use pie charts to represent the proportion of employees in different departments.
# Plot histogram to visualize the distribution of salaries
plt.hist(df_handeled['TotalPay'], edgecolor='black')
plt.title('Distribution of Salaries')
plt.xlabel('Total Pay')
plt.ylabel('Frequency')
plt.show()

# Plot pie chart to represent the proportion of employees in different departments
department_counts = df['JobTitle'].value_counts()
department_counts.plot(kind='pie')
plt.title('Proportion of Employees in Different Departments')
plt.show()


# 5-Grouped Analysis: Group the data by one or more columns and calculate summary statistics for each group, and compare the average salaries across different groups.
# grouping by JobTitle
grouped_data = df_handeled.groupby('JobTitle')
summary_statistics = grouped_data['TotalPay'].agg(['count', 'mean', 'median', 'min', 'max', 'std'])
summary_statistics


# 6-Simple Correlation Analysis: Identify any correlation between salary and another numerical column, and plot a scatter plot to visualize the relationship.
correlation = df_handeled['TotalPay'].corr(df_handeled['Year'])

# Print the correlation coefficient
print(f"Correlation between TotalPay and Years : {correlation:.2f}")

# Create a scatter plot
plt.scatter(x=df_handeled['Year'], y=df_handeled['TotalPay'])
plt.xlabel('Years')
plt.ylabel('Salary')
plt.title('TotalPay vs Years')
plt.show()


# 7-Summary of Insights: Write a brief report summarizing the findings and insights from the analyses.

# The dataset encompasses 148,654 records and 13 columns, providing a detailed perspective on employee compensation. Columns include a mix of numerical and categorical data types, with a notable presence of missing values in 'Benefits', 'Status' and 'Notes.'
# The distribution of 'TotalPay' exhibits a right-skewed pattern, indicating that a majority of employees receive moderate to lower salaries, with a smaller group earning higher compensation.
# Key statistics reveal a mean salary of $74,768.32, a median of $71,426.61, and a standard deviation of $50,517.01.
# The mode salary is observed at $0.00, suggesting a presence of employees with no reported pay.
# The minimum salary is noted as -618.13, indicating potential anomalies or errors in the data that require further investigation.
# The maximum salary is $567,595.43, contributing to a wide salary range of $568,213.56.
