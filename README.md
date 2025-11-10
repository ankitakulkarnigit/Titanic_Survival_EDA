# 🧭 EDA on Titanic Tragedy Survival 

## 📘 Project Overview
This project performs a **comprehensive Exploratory Data Analysis (EDA)** on the **Titanic dataset**, uncovering the key factors that influenced passenger survival.  
It walks through every stage — from **data loading and cleaning** to **feature engineering** and **visualization** — supported by theoretical insights at each step.  
The notebook serves as a complete, beginner-friendly guide for understanding how to explore and interpret real-world data.

---

## 🎯 Objective
To identify the factors that determined passenger survival aboard the Titanic and demonstrate the end-to-end EDA process used in data science projects.

---

## 🧠 What is EDA?
Exploratory Data Analysis (EDA) is the process of analyzing datasets to summarize their main characteristics using both **statistical** and **visual** methods.  
It helps data scientists:
- Understand the structure and relationships in data  
- Detect missing values, outliers, and anomalies  
- Guide data cleaning and feature selection for modeling  
- Build domain intuition before applying machine learning  

---

## ⚙️ Key Steps in the Notebook

| Step | Stage | Description |
|------|--------|-------------|
| 1️⃣ | **Setup & Libraries** | Import essential Python libraries: `pandas`, `numpy`, `matplotlib`, and `seaborn`. |
| 2️⃣ | **Data Loading & Inspection** | Load Titanic data, check shape, datatypes, and identify missing values. |
| 3️⃣ | **Data Cleaning** | Impute missing values (Age, Embarked) and engineer new indicator for missing Cabin info. |
| 4️⃣ | **Univariate Analysis** | Study distributions of numerical and categorical variables using histograms and countplots. |
| 5️⃣ | **Bivariate Analysis** | Explore how each feature (Sex, Pclass, Age, etc.) relates to survival. |
| 6️⃣ | **Feature Engineering** | Create new meaningful features — `FamilySize`, `IsAlone`, and `Title`. |
| 7️⃣ | **Multivariate Analysis** | Study interactions among multiple features (e.g., Sex × Pclass × Survival). |
| 8️⃣ | **Correlation Analysis** | Visualize numerical correlations with a heatmap. |
| 9️⃣ | **Automated Profiling** | Generate a detailed `ydata-profiling` report for dataset insights. |
| 🔟 | **Conclusion** | Summarize key findings and survival patterns. |

---

## 📊 Core Insights
- **Sex & Title** were the strongest predictors — females and children had the highest survival rates.  
- **Class disparity:** 1st class passengers had the best survival odds, while 3rd class fared the worst.  
- **Family size:** Small families (2–4) survived more often; being alone reduced survival chances.  
- **Fare & Cabin:** Higher fares and cabin availability correlated strongly with survival.  

---

## 🧩 Libraries Used
- **pandas** – Data manipulation & cleaning  
- **numpy** – Numerical computation  
- **matplotlib / seaborn** – Statistical visualization  
- **ydata-profiling** – Automated exploratory data profiling  

---

## 📁 Project Structure
```
├── Titanic_Survival_EDA.ipynb       # Main EDA notebook
├── sample.html                      # ydata-profiling report
├── README.md                        # Project documentation
└── Datasets/
    └── Titanic_Dataset.csv
```

---

## 🧾 Output Example
- Interactive plots (histograms, barplots, violin plots)
- Feature-engineered dataset (`FamilySize`, `IsAlone`, `Title`)
- Correlation heatmap
- Automated profiling report (`sample.html`)

---

## 🚀 How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/ankitakulkarnigit/Titanic_Survival_EDA.git
   cd Titanic_Survival_EDA
   ```
2. Install dependencies  
   ```bash
   pip install pandas numpy matplotlib seaborn ydata-profiling
   ```
3. Open the notebook  
   ```bash
   jupyter notebook Titanic_Survival_EDA.ipynb
   ```
4. Run all cells sequentially to reproduce the analysis.

---

## 🧩 Key Learnings
- Systematic EDA workflow from raw data → insights  
- Handling missing data, feature extraction, and variable relationships  
- Visual storytelling with data  
- Generating automated profiling reports for quick understanding  

---

## 🧠 Future Scope
- Apply machine learning (e.g., Logistic Regression, Random Forest) using engineered features.  
- Experiment with advanced visualizations or interactive dashboards (e.g., Plotly, Streamlit).  

---

## 👩‍💻 Author
**Ankita Kulkarni**  
*Data & AI Engineer | Exploring patterns in data and building intelligent systems.*  
📍 GitHub: [ankitakulkarnigit](https://github.com/ankitakulkarnigit)
