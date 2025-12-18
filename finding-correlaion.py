import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv'
data_url = 'survey_data.csv'
df = pd.read_csv(data_url)
# print(df.info())

# Task 1 – How are salaries spread out among respondents?

plt.figure(figsize = (8,5))
plt.hist(df['ConvertedCompYearly'], bins=50)
plt.title("Distribution of Yearly Compensation")
plt.xlabel("Yearly Compensation")
plt.ylabel("Number of Respondents")
plt.show()

# Task 2 – What is the typical salary (Median) for full-time employees?
full_time_df = df[df['Employment'] == 'Employed, full-time']

# Calculate median salary
median_salary = full_time_df['ConvertedCompYearly'].median()
print("Median salary (full-time):", median_salary)

# Task 3 - How does salary differ from country to country?
plt.figure(figsize=(8,5))
sns.boxplot(x='Country', y='ConvertedCompYearly', data=df)
plt.xticks(rotation=90)
plt.title("Compensation Distribution by Country")
plt.show()

# Task 4 - Remove Outliers from Salary Data - for - clean salary data

# Calculate IQR bounds
Q1 = df['ConvertedCompYearly'].quantile(0.25)
Q3 = df['ConvertedCompYearly'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Create refined dataset (without outliers)
df_clean = df[
    (df['ConvertedCompYearly'] >= lower_bound) &
    (df['ConvertedCompYearly'] <= upper_bound)
]

# Task 5 – Correlation Between Salary, Experience, and Satisfaction
# Are salary, experience, and job satisfaction related?

# get only three column and put them in new dataset
corr_df = df_clean[['ConvertedCompYearly', 'WorkExp', 'JobSatPoints_1']]

# Calculate correlation matrix
correlation = corr_df.corr()
print(correlation)

# Task 6 – Scatter Plot: Salary vs Experience
# Scatter plot

plt.figure(figsize=(6,4))
sns.scatterplot(
    x='WorkExp',
    y='ConvertedCompYearly',
    data=df_clean
)
plt.title("Salary vs Work Experience")
plt.xlabel("Work Experience (Years)")
plt.ylabel("Yearly Compensation")
plt.show()

# Task 7 – Scatter Plot: Salary vs Job Satisfaction
plt.figure(figsize=(6,4))
sns.scatterplot(
    x='JobSatPoints_1',
    y='ConvertedCompYearly',
    data=df_clean
)
plt.title("Salary vs Job Satisfaction")
plt.xlabel("Job Satisfaction Score")
plt.ylabel("Yearly Compensation")
plt.show()

