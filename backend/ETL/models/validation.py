import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from typing import Tuple


def kfold_cv(
        clf,
        X: pd.DataFrame,
        y: pd.Series,
        cv: int = 10,
        random_state : int = 42
        ) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Perform stratified K-fold cross-validation and return out-of-fold predictions.
    Parameters
    ----------
    X : pandas.DataFrame or numpy.ndarray
        Feature matrix.
    y : pandas.Series or numpy.ndarray
        Labels.
    clf : sklearn-like estimator
        Classifier implementing fit/predict (optionally predict_proba/decision_function).
    cv : int
        Number of folds (default 10)
    random_state : int
        RNG seed for shuffling (default 42).

    Returns
    -------
    (pandas.DataFrame
        DataFrame aligned with input order containing:
        - fold: which fold each sample served as validation
        - y_true: true label
        - y_pred: out-of-fold predicted class
        - y_proba: probability for the positive class (if available), else NaN
    ,
    pandas.DataFrame
        Dataframe containing the metrics for each fold:
        - accuracy: accuracy score
        - precision: precision score
        - recall: recall score
        - f1: F1 score (if available)
    )
    """

    oof_records = []
    fold_metrics_list = []
    current_fold = 0

    kfold = StratifiedKFold(
        n_splits=cv,
        shuffle=True,
        random_state=random_state
    )

    for train_index, test_index in kfold.split(X, y):
        current_fold += 1


        X_train = X.iloc[train_index]
        y_train = y.iloc[train_index]

        X_test = X.iloc[test_index]
        y_test = y.iloc[test_index]

        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        y_proba = clf.predict_proba(X_test)[:,1]

        oof_fold = pd.DataFrame({
            "fold": current_fold,
            "y_true": y_test,
            "y_pred": y_pred,
            "y_proba": y_proba},
            index=X_test.index)
        oof_records.append(oof_fold)

        fold_metrics = {
            "fold": current_fold,
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1": f1_score(y_test, y_pred)
        }
        fold_metrics_list.append(fold_metrics)

    oof_dp = pd.concat(oof_records).sort_index()
    metrics_dp = pd.DataFrame(fold_metrics_list)

    return oof_dp, metrics_dp




