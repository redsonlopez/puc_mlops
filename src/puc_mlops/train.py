import os
import random

import mlflow
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def reset_seeds():
    os.environ['PYTHONHASHSEED'] = str(42)
    np.random.seed(42)
    random.seed(42)


def read_data():
    data = pd.read_csv(
        'data/fetal_health_reduced.csv'
    )
    X = data.drop(["fetal_health"], axis=1)
    y = data["fetal_health"]
    return X, y


def process_data(X, y):
    columns_names = list(X.columns)
    scaler = preprocessing.StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_df = pd.DataFrame(X_scaled, columns=columns_names)

    X_train, X_test, y_train, y_test = train_test_split(
        X_df, y, test_size=0.3, random_state=42
    )

    # Ajuste se os valores do alvo forem 1, 2, 3
    y_train = y_train - 1
    y_test = y_test - 1
    return X_train, X_test, y_train, y_test


def create_model():
    reset_seeds()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    return model


def config_mlflow():
    os.environ['MLFLOW_TRACKING_USERNAME'] = 'redsonlopez'
    os.environ['MLFLOW_TRACKING_PASSWORD'] = 'e5d3980c463b148f5230380ed4ed8ce3f677db91'
    mlflow.set_tracking_uri('https://dagshub.com/redsonlopez/puc_mlops.mlflow')
    mlflow.sklearn.autolog(log_input_examples=True, log_model_signatures=True)


def train_model(model, X_train, y_train, is_train=True):
    with mlflow.start_run(run_name='experiment_puc_mlops') as run:
        model.fit(X_train, y_train)
        #if is_train:
            #run_uri = f'runs:/{run.info.run_id}'
            #mlflow.register_model(run_uri, 'fetal_health')


if __name__ == "__main__":
    X, y = read_data()
    X_train, X_test, y_train, y_test = process_data(X, y)
    model = create_model()
    config_mlflow()
    train_model(model, X_train, y_train)

