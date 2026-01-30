# Customer Churn Analytics Platform

This project focuses on building an **end-to-end data and analytics system** to analyze and predict customer churn in a subscription-based service. The primary goal is to identify high-risk customers before they leave, enabling the business to deploy **targeted, proactive retention strategies**.

While the project began as a traditional machine learning task, it has evolved into a **full data pipeline and backend-driven analytics platform**, integrating data engineering, backend development, and applied machine learning.

---

## Project Overview

This project addresses a classic **supervised binary classification problem** (`Churn: Yes / No`) using real-world telecom customer data. Multiple models are explored and evaluated, with a focus on **interpretability**, **robust evaluation**, and **business usability**.

Beyond modeling, the project emphasizes:
- Data cleaning and transformation
- Relational data storage in PostgreSQL
- API-based access to data via FastAPI
- A simple frontend interface for querying and exploration

**Reference Dataset:**  
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

**Target Variable:**  
`Churn (Yes / No)`

---

## Key Features

### Data Engineering
- Cleaned and transformed raw telecom customer data using Pandas
- Normalized categorical features and validated schema consistency
- Loaded processed data into a **local PostgreSQL database**
- Verified data integrity through SQL-based validation queries

### Backend Development
- Built a **FastAPI backend** to expose REST endpoints for querying PostgreSQL
- Implemented database queries and returned structured JSON responses
- Served static frontend assets (HTML, CSS, JavaScript) directly from the API
- Designed endpoints to support incremental expansion toward analytics and inference

### Frontend (Learning-Oriented)
- Developed a minimal web interface using vanilla HTML, CSS, and JavaScript
- Used the Fetch API to retrieve live data from backend endpoints
- Displayed query results dynamically in the browser for improved usability
- Focused on learning fundamentals rather than frameworks

### Machine Learning
- Conducted exploratory data analysis to identify churn drivers (e.g., contract type, monthly charges)
- Trained and evaluated multiple models using **Stratified K-Fold Cross-Validation**
- Addressed class imbalance with weighted loss functions
- Optimized performance using **F1-Macro**
- Selected **Logistic Regression** for interpretability and business relevance

---

## Environment Separation Philosophy

This project intentionally uses **two separate Python environments** to reflect real-world production practices.

### Research Environment (Conda)
Used for:
- Exploratory data analysis (EDA)
- Feature engineering
- Model training and evaluation
- Hyperparameter tuning

Includes heavier data science dependencies:
- NumPy
- Pandas
- Scikit-learn

This environment ensures stable numerical and scientific computing dependencies.

---

### Backend Environment (venv)
Used for:
- Serving data and analytics via API
- Querying PostgreSQL
- (Future) model inference

This environment is kept lightweight to:
- Reduce dependency conflicts
- Improve reliability
- Mirror production-style deployment constraints

**Training and serving are intentionally separated** to prevent dependency issues and enforce clean system boundaries.

---

## Environment Setup

### Create the Research Environment
If not already created:

```bash
conda env create -f notebooks/environment.yml
conda activate churn-research
