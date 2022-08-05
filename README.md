# REST API для сервиса YaMDb

![example event parameter](https://github.com/ravimb06/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

REST API проект для сервиса YaMDb — собирает отзывы пользователей на произведения.
Произведения делятся на категории.
Пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти. Из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.
Сами произведения в YaMDb не хранятся

## Docker-compose
### Перейти в директорию с файлом docker-compose.yaml:
```bash
$ cd infra
```
### Запустить
```bash
$ docker-compose up -d --build
```

### Выполнить миграции
```bash
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
```
### Создаем суперпользователя
```bash
$ docker-compose exec web python manage.py createsuperuser 
```
### Собрать статику
```bash
$ docker-compose exec web python manage.py collectstatic --no-input
```
### Остановить контейнеры
```bash
$ docker-compose down -v
```
## Документация
```
http://127.0.0.1:8000/redoc/
```
### Использованные технологии:
- Python 3
- Django
- Django REST framework
- Docker

# Авторы:
- Али Богатырев. <https://github.com/ravimb06>
