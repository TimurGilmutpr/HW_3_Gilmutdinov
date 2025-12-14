ML Model Deployment with Blue-Green Strategy
📋 Описание проекта
Проект демонстрирует автоматизированное развертывание ML-модели с использованием стратегии Blue-Green Deployment и CI/CD пайплайна на GitHub Actions.

🚀 Быстрый старт
1. Клонирование и настройка
bash
git clone <your-repo-url>
cd ml-deployment-project
2. Запуск всех сервисов
bash
docker-compose -f docker-compose.yml -f docker-compose.blue.yml -f docker-compose.green.yml up --build -d
3. Проверка работы
bash
# Проверка Blue версии (v1.0.0)
curl http://localhost:8081/health

# Проверка Green версии (v1.1.0)
curl http://localhost:8082/health

# Проверка через Nginx
curl http://localhost/health
🏗️ Архитектура
Blue Service: Версия v1.0.0 модели (порт 8081)

Green Service: Версия v1.1.0 модели (порт 8082)

Nginx: Балансировщик нагрузки (порт 80)

📡 API Эндпоинты
Health Check
bash
GET /health
Ответ:

json
{"status": "ok", "version": "v1.0.0"}
Предсказание
bash
POST /predict
Content-Type: application/json

{
  "features": [[1], [2], [3]]
}
Ответ:

json
{
  "predictions": [...],
  "model_version": "v1.0.0"
}
🔄 Управление развертыванием
Переключение трафика
bash
# Переключить на Blue
./scripts/switch_traffic.sh

# Переключить на Green
./scripts/switch_traffic.sh
Проверка статуса
bash
# Статус всех сервисов
docker-compose -f docker-compose.yml -f docker-compose.blue.yml -f docker-compose.green.yml ps

# Логи Blue
docker logs ml-service-blue

# Логи Green
docker logs ml-service-green
🛠️ CI/CD Pipeline
GitHub Actions автоматически:

Тестирует код при пуше в main/develop

Собирает Docker образ

Публикует образ в GitHub Container Registry

Выполняет деплой

Настройка секретов:
Settings → Secrets and variables → Actions

Добавьте:

GITHUB_TOKEN (автоматически)

DOCKERHUB_TOKEN (опционально)

📁 Структура проекта
text
ml-deployment-project/
├── app/                    # Исходный код приложения
├── docker/                 # Конфигурация Nginx
├── scripts/               # Скрипты управления
├── docker-compose.yml     # Основной конфиг
├── docker-compose.blue.yml # Blue версия
├── docker-compose.green.yml # Green версия
├── Dockerfile            # Конфигурация Docker
└── .github/workflows/    # CI/CD пайплайны
🧪 Тестирование
Локальное тестирование
bash
# Запуск тестового запроса
curl -X POST http://localhost/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [[1], [2], [3]]}'
Проверка health check
bash
./scripts/health_check.sh
🚨 Устранение неполадок
Сервисы не запускаются
bash
# Проверьте логи
docker-compose logs

# Пересоберите образы
docker-compose up --build -d
Проблемы с сетью
bash
# Проверьте сеть
docker network inspect ml-network
Nginx не переключает трафик
bash
# Перезапустите Nginx
docker-compose restart nginx
📊 Мониторинг
Версия модели: Возвращается в каждом ответе

Статус сервиса: Эндпоинт /health

Логи: Доступны через docker-compose logs

🔧 Зависимости
Docker & Docker Compose

Python 3.11+

FastAPI, Uvicorn, Scikit-learn


