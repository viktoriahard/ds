import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def load_data(file_path):
    return pd.read_csv(file_path)


def preprocess_data(df, target_column):
    x = df.drop(columns=[target_column])
    y = df[target_column]

    numeric_features = ['CustomerID', 'Age', 'Annual Income (k$)', 'Spending Score (1-100)']
    categorical_features = ['Genre']
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    x_processed = preprocessor.fit_transform(x)
    return x_processed, y, preprocessor


def train_model(x, y):

    model = LinearRegression()
    model.fit(x, y)
    return model


def predict(model, x):
    return model.predict(x)


def evaluate_model(y_true, y_pred):

    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return mse, r2