#!/bin/bash

# Скрипт для переключения трафика между blue и green

set -e

NGINX_CONF="docker/nginx.conf"
BLUE_SERVICE="blue:8080"
GREEN_SERVICE="green:8080"

echo "Текущая конфигурация Nginx:"
grep -A2 "upstream backend" $NGINX_CONF

echo ""
echo "Выберите действие:"
echo "1) Переключить весь трафик на Blue (v1.0.0)"
echo "2) Переключить весь трафик на Green (v1.1.0)"
echo "3) Распределить трафик 50/50"
read -p "Ваш выбор (1-3): " choice

case $choice in
    1)
        echo "Переключаем весь трафик на Blue..."
        sed -i "s/server .*:8080;/server $BLUE_SERVICE;/" $NGINX_CONF
        ;;
    2)
        echo "Переключаем весь трафик на Green..."
        sed -i "s/server .*:8080;/server $GREEN_SERVICE;/" $NGINX_CONF
        ;;
    3)
        echo "Распределяем трафик 50/50..."
        sed -i "s/server .*:8080;/server $BLUE_SERVICE;\n        server $GREEN_SERVICE;/" $NGINX_CONF
        ;;
    *)
        echo "Неверный выбор"
        exit 1
        ;;
esac

# Перезагружаем Nginx
docker-compose exec nginx nginx -s reload 2>/dev/null || echo "Перезапустите nginx вручную: docker-compose restart nginx"

echo "Конфигурация обновлена!"
echo "Новая конфигурация:"
grep -A3 "upstream backend" $NGINX_CONF
