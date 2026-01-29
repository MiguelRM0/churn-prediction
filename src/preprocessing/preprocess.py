import pandas as pd
from src.config import CATEGORICAL_COLUMNS, INTEGER_COLUMNS, FLOAT_COLUMNS
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from typing import Tuple





def preprocess(df: pd.DataFrame, X: pd.DataFrame, y: pd.Series) -> Tuple[pd.DataFrame, pd.Series]:
    numerical_cols = INTEGER_COLUMNS + FLOAT_COLUMNS

    preprocessor = ColumnTransformer(
        transformers=[("numeric", StandardScaler(), numerical_cols,
                       "categorical", OneHotEncoder(), CATEGORICAL_COLUMNS)]
        )
    x_scaled = preprocessor.fit_transform(X)

    X = pd.DataFrame(x_scaled, columns = preprocessor.get_feature_names_out())
    y = y.cat.codes 
    return X,y

