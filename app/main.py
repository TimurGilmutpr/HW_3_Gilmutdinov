from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import os
from model.model import model
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="ML Model Service", version=os.getenv("MODEL_VERSION", "v1.0.0"))

# Модель для входных данных
class PredictionRequest(BaseModel):
    features: list[list[float]]
    
class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/health", response_model=HealthResponse)
async def health():
    """Проверка здоровья сервиса"""
    return {
        "status": "ok",
        "version": os.getenv("MODEL_VERSION", "v1.0.0")
    }

@app.post("/predict")
async def predict(request: PredictionRequest):
    """Эндпоинт для предсказаний"""
    try:
        logger.info(f"Получен запрос на предсказание, версия: {model.version}")
        
        # Преобразуем данные в numpy array
        data = np.array(request.features)
        
        # Получаем предсказания
        predictions = model.predict(data)
        
        return {
            "predictions": predictions,
            "model_version": model.version,
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Ошибка при предсказании: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "message": "ML Model Service",
        "version": os.getenv("MODEL_VERSION", "v1.0.0"),
        "endpoints": ["/health", "/predict"]
    }
