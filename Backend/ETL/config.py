DROP_COLUMNS =[
    "customerID"
]

TARGET_COLUMNS= [
    "Churn"
]

CATEGORICAL_COLUMNS = [
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod"
]

INTEGER_COLUMNS = [
    "tenure"
]

FLOAT_COLUMNS = [
    "MonthlyCharges", 
    "TotalCharges"
]

# Parameters gotten from notebooks hyperparameter tunning
LOGISTICREG_PARAMS = {
    "class_weight" : "balanced",
    "max_iter": 10000,
    "solver": "sage",
    "C":0.01,
    "random_state": 42
}

RANDOMFOREST_PARAM = {
    "criterion":"entropy",
    "class_weight":"balanced_subsample",
    "max_depth": 10,
    "min_sample_split":2,
    "n_estimators":400
}