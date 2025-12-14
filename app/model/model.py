import joblib
import numpy as np
from sklearn.linear_model import LinearRegression
import os

class MLModel:
    def __init__(self, version="v1.0.0"):
        self.version = version
        self.model = self._create_dummy_model()
        
    def _create_dummy_model(self):
        """Создаем демо-модель для примера"""
        model = LinearRegression()
        # Обучаем на простых данных
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([2, 4, 6, 8, 10])
        model.fit(X, y)
        return model
        
    def predict(self, data):
        """Предсказание на новых данных"""
        return self.model.predict(data).tolist()
        
    def save(self, path):
        """Сохранение модели"""
        joblib.dump(self.model, path)
        
    def load(self, path):
        """Загрузка модели"""
        self.model = joblib.load(path)

# Создаем экземпляр модели
model = MLModel(os.getenv("MODEL_VERSION", "v1.0.0"))
