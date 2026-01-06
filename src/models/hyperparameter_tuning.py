import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold

# Grab best parameters create a new model where we will do a test and get ROC curve then explain those
def grid_cv(X, y, clf, paramgrid ,cv = 10, shuffle = True, random_state = 42 , n_jobs = -1):
    """
     Perform cross validation using GridSearchCV to fine tune hyperparameters

    Parameters
    ----------
    X : pandas.DataFrame or numpy.ndarray
        Feature matrix.
    y : pandas.Series or numpy.ndarray
        Labels.
    clf : sklearn-like estimator
        Classifier implementing fit/predict
    cv : int
        Number of folds (default 10).
    shuffle : bool
        Shuffle before splitting (default True).
    random_state : int
        RNG seed for shuffling (default 42).
    paramgrid: dict [str, list] {  param_name : param_values }
        Param_name a str representing the name of the parameter to optimize.
        param_values a list of values to be tested for corresponding parameter
    n_jobs: int (default -1)
        Number of jobs to run in parallel.
    Returns
    -------
    dict
        {
            'best_estimator': fitted model with best f1_macro,
            'best_params': best hyperparameters,
            'best_f1_macro': best f1_macro score,
            'best_accuracy': accuracy corresponding to best f1_macro,
            'cv_results': full cross-validation results
        }
    """
    kfold = StratifiedKFold(n_splits=cv, shuffle=shuffle, random_state=random_state)
    grid = GridSearchCV(clf, param_grid=paramgrid, cv=kfold, scoring=["accuracy", "f1_macro"], refit="f1_macro", n_jobs=n_jobs)
    grid.fit(X, y)
    best_model = grid.best_estimator_

    return {
        'best_model': best_model, # Best model object
        'best_params': grid.best_params_,
        'best_f1_macro': grid.best_score_,
        'cv_results': grid.cv_results_,
        }


