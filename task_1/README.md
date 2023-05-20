## Задача 1

Проект написан на FastApi, б.д. postgres. Можно развернуть с помощью docker-compose.

Для запуска проекта, скачать репозиторий, из данной директории выполнить следующие команды.

```
docker compose up -d
```
Если проект разворачивается первый раз, запустить выполнение миграций.
```
docker compose exec backend alembic upgrade head
```

Документация будет доступна по ссылке: http://localhost:8000/docs

POST запрос для пополнения вопросов в базу на: http://localhost:8000/question/

GET запрос для получения сохраненных вопросов на: http://localhost:8000/question/
