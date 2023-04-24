# Highload Nginx

## Nginx

## App
Простое Python приложение на фреймворке Flask.

## Яндекс Танк
Докуменатция
https://yandextank.readthedocs.io/en/latest/index.html 
### Подготовка
Необходимо получить api token.
Зарегистрироватьсян на сайте https://overload.yandex.net/.  
В настройках профиля "Your api token".

Переименовать файл token.txt_sample в token.txt и прописать ключ.

### Настройка
Для настройки теста см. файл yandex_tank/load.yaml

### Запуск
```
docker exec -ti tank yandex-tank -c load.yaml
```
### Просмотр отчета

Веб версия отчета доступна в личном кабинете https://overload.yandex.net/ 

