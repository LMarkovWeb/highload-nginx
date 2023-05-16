# Highload Nginx

## Nginx
Контейнер nginx:latest с минимальным конфигом (nginx/default.conf).  
Настроен upstream на приложение на Python:
```
upstream app {
    server app:5000;
}
```
где app - это имя контейнера Docker.  

## GoAccess
Анализатор логов в режиме реального времени. Может работать с логами доступа Nginx (access.log).  
https://goaccess.io/  
Поднят в отдельном контейнере и имеет доступ к папке с логами nginx (data/logs/nginx) на хосте.

## App
Простое Python приложение на фреймворке Flask.

## Яндекс Танк
Нагрузочное тестирование.  
Документация https://yandextank.readthedocs.io/en/latest/index.html 
### Подготовка
Необходимо получить api token.
Зарегистрироватьсян на сайте https://overload.yandex.net/.  
В настройках профиля "Your api token".

Скопировать файл token.txt_sample в token.txt и прописать ключ.

### Настройка
Для настройки теста см. файл yandex_tank/load.yaml

### Запуск
```
docker exec -ti tank yandex-tank -c load.yaml
```
### Просмотр отчета
Веб версия отчета доступна в личном кабинете https://overload.yandex.net/ 

## Команды быстрого управления
Файл Makefile.  
Запуск команд:
```
make start
make stop
#etc
```