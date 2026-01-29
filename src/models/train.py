
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import LogisticRegression
from src.data.clean import downcasting, categories 
from src.config import CATEGORICAL_COLUMNS, FLOAT_COLUMNS, INTEGER_COLUMNS


pandas_cleaning_step = FunctionTransformer(downcasting, validate=False)
category_step = FunctionTransformer(categories, validate=False)


numeric_features = FLOAT_COLUMNS + INTEGER_COLUMNS

# Create the transformer for math
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse=False), CATEGORICAL_COLUMNS)
    ])

# --- STEP 3: Combine everything into one master Pipeline ---
pipe = Pipeline(steps=[
    ('downcast', pandas_cleaning_step),  # Runs your downcasting function
    ('fix_cats', category_step),        # Runs your categorical conversion
    # Save one data of the cleaned data 
    ('math_prep', preprocessor),        # Does the Scaling and One-Hot Encoding
    # Save the read_for_modeling data
])