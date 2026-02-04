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

### Docker (Backend API — Current Setup)
The backend API is containerized. The database is **still local for now** and will be
dockerized later.

1. Create a `.env` file (or copy `.env.example`) and set these values:

```bash
DB_HOST=host.docker.internal
DB_NAME=churn_data
DB_USER=your_user
DB_PASSWORD=your_password
DB_PORT=5432
API_PORT=8000
```

2. Build the image from the project root:

```bash
docker build -t churn-backend -f backend/Dockerfile .
```

3. Run the container:

```bash
docker run --rm -p 8000:8000 --env-file .env churn-backend
```

4. Open the app at `http://localhost:8000`.

**Note:** `host.docker.internal` works on macOS/Windows to reach the host database.
On Linux, use your host IP or Docker's host gateway.

---

### Research Environment (Conda)
Used for EDA and model training.

```bash
conda env create -f notebooks/environment.yml
conda activate churn-research
```

---

### Backend Environment (Local venv)
If you prefer running the API locally without Docker:

```bash
python -m venv backend/venv
source backend/venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Make sure your `.env` file is present so the API can connect to PostgreSQL.

---

## Planned: Dockerized Database
The PostgreSQL database is currently running on the host machine. A Dockerized DB
setup (likely via `docker-compose`) is planned next so the API and DB can run
entirely in containers.
