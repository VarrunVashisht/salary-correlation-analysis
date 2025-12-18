# 📊 Developer Salary Analysis (Correlation) from Survey Data

## 📌 Overview

This project performs **exploratory data analysis (EDA)** on survey data to understand **developer salary trends**.
It answers common questions such as:

* How are salaries distributed?
* What is the typical (median) salary for full-time employees?
* How do salaries vary by country?
* How are salary, experience, and job satisfaction related?

The analysis is done using **Python**, with popular data science libraries like **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 🧰 Tools & Libraries Used

* **Python**
* **Pandas** – data loading and manipulation
* **Matplotlib** – basic plotting
* **Seaborn** – advanced and cleaner visualizations

---

## 📂 Dataset

* **File:** `survey_data.csv`
* **Key Columns Used:**

  * `ConvertedCompYearly` – yearly compensation
  * `Employment` – employment type
  * `Country` – respondent’s country
  * `WorkExp` – years of work experience
  * `JobSatPoints_1` – job satisfaction score

> ⚠️ Make sure the dataset is present in the project root directory before running the script.

---

## 📝 Analysis Tasks Performed

### 1️⃣ Salary Distribution

* Plotted a **histogram** to visualize how yearly compensation is spread among respondents.

### 2️⃣ Median Salary for Full-Time Employees

* Filtered only **full-time employees**
* Calculated the **median yearly salary**

### 3️⃣ Salary Comparison by Country

* Created a **boxplot** to compare salary distributions across different countries.

### 4️⃣ Outlier Removal

* Removed extreme salary values using the **Interquartile Range (IQR)** method.
* Created a cleaned dataset for more reliable analysis.

### 5️⃣ Correlation Analysis

* Examined relationships between:

  * Salary
  * Work experience
  * Job satisfaction
* Generated a **correlation matrix**.

### 6️⃣ Salary vs Work Experience

* Used a **scatter plot** to visualize how salary changes with years of experience.

### 7️⃣ Salary vs Job Satisfaction

* Used a **scatter plot** to explore the relationship between salary and job satisfaction scores.

---


## 📈 Output

* Multiple visualizations (histograms, boxplots, scatter plots)
* Console output showing:

  * Median salary
  * Correlation matrix

---

## 🎯 Purpose of This Project

This repository is ideal for:

* Beginners learning **data analysis & visualization**
* Practicing **EDA techniques**
* Portfolio demonstration for **data analyst / data science roles**

---

##  Author
Varrun Vashisht




