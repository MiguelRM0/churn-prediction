## Customer Churn Prediction
This project will go in depth in to creating a model to predict customer retention rate on a service. The primary goal isto identify high-risk customers before they leave, enabling the business to deploy targeted, proactive retention strategies.

## Description
This project addresses a classic supervised **binary classification problem**. This solution leverages **multiple models** along with meticulous **hyperparameter tuning** to create an interpretable **machine learning** model to achieve high-accuracy
predictions and provide **actionable** business insights. 
* **Reference Data Source:** https://www.kaggle.com/datasets/blastchar/telco-customer-churn
* **Target Variable:** Churn (Yes/No)



---

## Environment Separation Philosophy

This project uses **two separate Python environments** by design:

### Research Environment (Conda)
- Used for:
  - Data exploration
  - Feature engineering
  - Model training and evaluation
  - Hyperparameter tuning
- Contains heavier data science dependencies (NumPy, Pandas, Scikit-learn, etc.)
- Ensures consistent and stable binary dependencies for numerical computing

### Backend Environment (venv)
- Used for:
  - Serving predictions via an API
  - Loading pre-trained models
- Kept lightweight to reduce complexity and runtime overhead
- Only includes dependencies required for inference

> **Training and serving are intentionally separated** to prevent dependency conflicts and improve reliability.

---

### Create the Research Environment
If you do not already have the environment:

```bash
conda env create -f research/environment.yml
conda activate churn-research
```

### Create Virtual Environment
```bash
cd Backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Authors and acknowledgment
by Miguel Romero

## Project status
**Active:** Want to extend the explainability of the features and there importance. Want make a simple website where you can enter a observation and it makes a prediction. This will be built with simple HTML,CSS along with a REST API(FAST API). 
