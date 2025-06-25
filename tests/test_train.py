import pandas as pd
import pytest
from sklearn.base import ClassifierMixin
from puc_mlops.train import (
    read_data,
    create_model,
    train_model
)


@pytest.fixture
def sample_data():
    """
    A fixture function that returns a sample dataset.

    Returns:
        pandas.DataFrame: A DataFrame containing sample data with two features and a target.
    """
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4, 5],
        'feature2': [6, 7, 8, 9, 10],
        'fetal_health': [1, 1, 2, 3, 2]
    })
    return data


def test_read_data():
    """
    Tests the `read_data` function to ensure that the features (X) and labels (y) are not empty.
    """
    X, y = read_data()
    assert not X.empty
    assert not y.empty


def test_create_model():
    """
    Tests that the model created is a scikit-learn classifier.
    """
    X, _ = read_data()
    model = create_model()
    assert isinstance(model, ClassifierMixin)


def test_train_model(sample_data):
    """
    Tests the `train_model` function using sample data and verifies the model was trained.
    """
    X = sample_data.drop(['fetal_health'], axis=1)
    y = sample_data['fetal_health'] - 1
    model = create_model()
    train_model(model, X, y, is_train=False)
    # O RandomForest não armazena histórico de treino, mas podemos verificar se ele aprendeu algo
    assert hasattr(model, "predict")
    predictions = model.predict(X)
    assert len(predictions) == len(y)

