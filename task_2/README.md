## Задача 2

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

Создание пользователя, POST запрос:  http://localhost:8000/users/

Получение пользователя по id, GET запрос:  http://localhost:8000/users/{id}/

Загрузка аудио файла .wav, POST запрос:  http://localhost:8000/upload/

Получение сконвертированного файла:  http://localhost:8000/record?id=id_записи&user=id_пользователя