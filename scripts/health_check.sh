#!/bin/bash

# Скрипт для проверки здоровья всех сервисов

echo "Проверка здоровья всех сервисов..."
echo ""

echo "1. Проверка Blue (v1.0.0):"
curl -s http://localhost:8081/health || echo "Blue сервис недоступен"
echo ""

echo "2. Проверка Green (v1.1.0):"
curl -s http://localhost:8082/health || echo "Green сервис недоступен"
echo ""

echo "3. Проверка через Nginx (текущий активный):"
curl -s http://localhost/health || echo "Nginx недоступен"
echo ""

echo "4. Тестовый запрос на предсказание:"
curl -s -X POST http://localhost/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [[1], [2], [3]]}' | jq . 2>/dev/null || \
  echo "Предсказание недоступно"
