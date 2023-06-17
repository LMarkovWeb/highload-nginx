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
Поднят в отдельном контейнере и имеет доступ к папке с логами nginx (nginx/logs) на хосте.
В этой же папке создается файл отчета 
```
nginx/logs/report.html
```
который можно просматривать в браузере.

## App
Простое Python приложение на фреймворке Flask.

## Яндекс Танк
Нагрузочное тестирование.  

### Подготовка
Необходимо получить api token.
Зарегистрироватьсян на сайте https://overload.yandex.net/.  
В настройках профиля "Your api token".

Скопировать файл token.txt_sample в token.txt и прописать ключ.

### Настройка
Для настройки теста см. файл yandex_tank/load.yaml

### Запуск
```
docker exec -ti tank yandex-tank -c load_*.yaml
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

## Ссылки

 - [Пример нагрузочного тестирования сайта с Yandex.Tank](https://serveradmin.ru/primer-nagruzochnogo-testirovaniya-sajta-s-yandex-tank/)
 - [Самый легкий способ составить README](https://readme.so/ru)
 - [GitHub yandex-tank](https://github.com/yandex/yandex-tank)
 - [Документация Яндекс Танк](https://yandextank.readthedocs.io/en/latest/index.html)
 - [Yandex.Tank: нагрузочное тестирование](https://rtfm.co.ua/ru/yandex-tank-nagruzochnoe-testirovanie/)
 - [Яндекс.Танк – организуем эффективную систему нагрузочного тестирования](https://vis.center/blog/support-24-7/yandeks-tank-organizuem-effektivnuyu-sistemu-nagruzochnogo-testirovaniya/)
 - [Яндекс.Танк и автоматизация нагрузочного тестирования](https://habr.com/ru/companies/pt/articles/204224/)
 - [Нагрузочное тестирование c Yandex.Tank и JMeter](https://gist.github.com/sameoldmadness/9abeef4c2125bc760ba2f09ee1150330)
 - [GoAccess for Nginx logs](https://goaccess.io/ )
 - [Nginx: worker_processes](http://nginx.org/ru/docs/ngx_core_module.html#worker_processes)
 - [Nginx: worker_connections](http://nginx.org/ru/docs/ngx_core_module.html#worker_connections)
 - [Nginx: Модуль ngx_http_log_module](http://nginx.org/ru/docs/http/ngx_http_log_module.html)
 - [Nginx: Все директивы](http://nginx.org/en/docs/dirindex.html)
 - [Nginx: Ускоряем Nginx за 5 минут](https://habr.com/ru/articles/198982/)