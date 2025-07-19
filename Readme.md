# 📊 LinkedIn Job Analysis Project

## 📌 Project Overview
This project presents an interactive analysis of LinkedIn job postings focused on Data Analyst and Data Scientist roles. The goal is to identify key hiring trends, popular locations, and the most in-demand technical skills using a Streamlit dashboard.

## 🚀 Live Dashboard  
[![View Live App](https://img.shields.io/badge/Streamlit-Live%20App-brightgreen?logo=streamlit)](https://linkedin-job-analysis-happ5gh6brnnuiraz75zbgo.streamlit.app/)

# ✅ Project Workflow Breakdown:

### 1. Project Planning & Dataset Selection
- 🧭 **Defined Project Scope**: Focused on **Data Analyst** and **Data Scientist** roles in **India** and **Remote** opportunities.
- 🔄 Initially planned to scrape data from LinkedIn, but later selected a **clean, pre-scraped dataset from Kaggle** for better accessibility and structure.

### 2. Environment Setup
- 🛠️ Created a **Python virtual environment** (`venv`) to manage project dependencies.
- 📂 Initialized a **Git repository** for version control.
- ☁️ Pushed the project to **GitHub**, ensuring a proper `.gitignore` was set up to exclude files like the virtual environment.

### 3. Dataset Understanding
- 📁 Loaded dataset: `ds_salaries.csv`
- 🔍 Explored key columns:
  - Job Title
  - Salary Estimate
  - Job Description
  - Location
  - Company Name
- ✅ Checked for missing values and ensured consistency.

### 4. Data Cleaning
- 🧹 Removed unnecessary columns like `Unnamed: 0` and `index`.
- ✅ Retained relevant fields: `Job Title`, `Job Description`, `Salary`, `Location`, `Company Name`.
- 🔍 Extracted key technical skills using **keyword matching**:
  - Python, SQL, Excel, Tableau, Machine Learning, R, Power BI, Hadoop, Spark, AWS

### 5. Exploratory Data Analysis (EDA)
- 📊 Performed analysis on:
  - 🔝 Top 10 most common job titles
  - 📍 Top 10 hiring locations
  - 💼 Most in-demand technical skills
- 🖼️ Visualized insights using **Matplotlib** and **Seaborn**.

### 6. Dashboard Development with Streamlit
- ⚙️ Built an **interactive dashboard** using **Streamlit**.
- ✨ Key Features:
  - 📊 Bar charts for job titles & locations
  - 🔎 Skill analysis from job descriptions
  - 🧭 Interactive sidebar filter to select locations
- 🧼 Designed a clean, user-friendly interface.

### 7. Deployment on Streamlit Cloud
- 🚀 Pushed the project to **GitHub**.
- ☁️ Deployed the dashboard to **Streamlit Cloud** for public access.

## 🎯 Key Features
✅ Real-time interactive dashboard using Streamlit

📌 Visualization of top job titles and hiring locations

📊 Skill analysis directly from job descriptions

🎛️ Sidebar filters for dynamic selection of locations

🛠️ Clean and modular Python code structure

## 🛠️ Tools & Technologies
Python: pandas, matplotlib, seaborn, streamlit

Data Analysis & Cleaning: pandas

Data Visualization: seaborn, matplotlib, Streamlit native charts

Dashboard Deployment: Streamlit Cloud

Version Control: Git & GitHub


## 📂 Project Structure
```text
LinkedIn-Job-Posting-Analysis/
│
├── data/                             # Raw and dataset
│   └── ds_salaries.csv
│
├── notebooks/                        # Jupyter Notebooks for EDA and preprocessing
│   └── linkedin_job_analysis.ipynb
│
├── dashboard.py                      # Streamlit dashboard code
├── requirements.txt                  # Project dependencies
├── README.md                         # Project documentation
└── .gitignore                        # Git ignored files and folders

```


## 💡 Future Improvements

🔄 Integrate real-time LinkedIn job scraping using APIs or Selenium

🌍 Expand analysis to cover more job roles and locations

💼 Add real-time salary benchmarks from external datasets


## ✨ Connect with Me
- [LinkedIn](https://www.linkedin.com/in/garv999/)
- [GitHub](https://github.com/garv999)

## ✨Author
Garv Agarwal
