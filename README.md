# PostCraft

> REST API-платформа для публикации постов, комментариев, тегов и
> пользовательских профилей на базе Django и Django REST Framework.

## О проекте

**PostCraft** — это backend-приложение для социальной платформы или
блог-сервиса, где пользователи могут:

- публиковать посты;
- добавлять комментарии;
- использовать категории и теги;
- управлять профилем;
- проходить аутентификацию и авторизацию;
- взаимодействовать с REST API.

Проект построен по модульной архитектуре Django-приложений и ориентирован на
дальнейшее масштабирование.

---

# Содержание

- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Функциональность](#функциональность)
- [Установка и запуск](#установка-и-запуск)
- [Настройка окружения](#настройка-окружения)
- [Миграции](#миграции)
- [Запуск сервера](#запуск-сервера)
- [API](#api)
- [Аутентификация](#аутентификация)
- [Права доступа](#права-доступа)
- [Примеры запросов](#примеры-запросов)
- [Безопасность](#безопасность)
- [Production рекомендации](#production-рекомендации)

---

# Технологии

Основной стек проекта:

- Python 3.x
- Django
- Django REST Framework
- SQLite / PostgreSQL
- JWT / Token Authentication
- Pillow (если используется работа с изображениями)

Дополнительно:

- Pagination
- Permissions
- Serializers
- REST API architecture
- Modular Django apps

---

# Структура проекта

```bash
PostCraft/
│
├── apps/
│   ├── authentication/
│   ├── categories/
│   ├── comments/
│   ├── posts/
│   ├── profiles/
│   ├── tags/
│   └── users/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── media/
├── manage.py
├── requirements.txt
└── .env
```

## Описание модулей

### `authentication`

Отвечает за:

- регистрацию пользователей;
- логин;
- токены доступа;
- сигналы пользователей;
- сериализацию auth-данных.

### `posts`

Основная бизнес-логика публикаций:

- CRUD постов;
- пагинация;
- permissions;
- сериализация;
- работа с категориями и тегами.

### `comments`

Функциональность комментариев:

- создание комментариев;
- редактирование;
- удаление;
- привязка к постам.

### `profiles`

Профили пользователей:

- аватар;
- описание;
- социальные данные;
- пользовательские настройки.

### `users`

Работа с пользователями:

- модели пользователей;
- permissions;
- API пользователей.

### `categories`

Категории для постов.

### `tags`

Система тегов.

---

# Функциональность

## Пользователи

- Регистрация
- Авторизация
- JWT / Token authentication
- Профили пользователей
- Редактирование данных

## Посты

- Создание постов
- Редактирование
- Удаление
- Просмотр списка
- Просмотр детальной информации
- Фильтрация
- Пагинация

## Комментарии

- CRUD комментариев
- Привязка к постам
- Автор комментария

## Категории и теги

- Создание категорий
- Назначение тегов
- Фильтрация по тегам

---

# Установка и запуск

## 1. Клонирование репозитория

```bash
git clone https://github.com/ValeriaPostylyakova/REST-API-PostCraft.git
```

---

## 2. Создание виртуального окружения

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

---

# Настройка окружения

Создайте файл `.env`:

```env
DEBUG=True
SECRET_KEY=your_secret_key

DB_NAME=postcraft
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

ADMIN_PANEL_PATH=your_url
```

Если используется SQLite — дополнительная настройка не требуется.

---

# Миграции

```bash
python manage.py makemigrations
python manage.py migrate
```

---

# Создание суперпользователя

```bash
python manage.py createsuperuser
```

---

# Запуск сервера

```bash
python manage.py runserver
```

После запуска сервер будет доступен:

```text
http://127.0.0.1:8000/
```

---

# API

Ниже приведены примерные эндпоинты проекта.

## Authentication

| Method | Endpoint              | Description       |
| ------ | --------------------- | ----------------- |
| POST   | `/api/auth/register/` | Регистрация       |
| POST   | `/api/auth/login/`    | Авторизация       |
| POST   | `/api/auth/refresh/`  | Обновление токена |

---

## Posts

| Method | Endpoint           | Description    |
| ------ | ------------------ | -------------- |
| GET    | `/api/posts/`      | Список постов  |
| POST   | `/api/posts/`      | Создание поста |
| GET    | `/api/posts/{id}/` | Детали поста   |
| PUT    | `/api/posts/{id}/` | Обновление     |
| DELETE | `/api/posts/{id}/` | Удаление       |

---

## Comments

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| GET    | `/api/comments/`      | Список комментариев  |
| POST   | `/api/comments/`      | Создание комментария |
| DELETE | `/api/comments/{id}/` | Удаление комментария |

---

## Categories

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | `/api/categories/` | Список категорий |

---

## Tags

| Method | Endpoint     | Description  |
| ------ | ------------ | ------------ |
| GET    | `/api/tags/` | Список тегов |

---

# Аутентификация

Проект может использовать:

- JWT Authentication
- DRF Token Authentication
- Session Authentication

Пример заголовка:

```http
Authorization: Bearer your_access_token
```

---

# Права доступа

В проекте используются кастомные permissions.

Примеры:

- Только автор может редактировать пост.
- Только автор может удалить комментарий.
- Администратор имеет полный доступ.
- Неавторизованный пользователь имеет только read-only доступ.

---

# Примеры запросов

## Создание поста

```http
POST /api/posts/
Content-Type: application/json
Authorization: Bearer token
```

```json
{
	"title": "My first post",
	"content": "Hello from PostCraft",
	"category": 1,
	"tags": [1, 2]
}
```

---

## Ответ

```json
{
	"id": 1,
	"title": "My first post",
	"content": "Hello from PostCraft"
}
```

---

# Безопасность

Перед production:

- отключить DEBUG;
- заменить SECRET_KEY;
- настроить HTTPS;
- заменить ADMIN_PANEL_PATH;
- использовать PostgreSQL;
- вынести секреты в environment variables.

---

# Production рекомендации

Рекомендуемый стек:

- Gunicorn
- Nginx
- PostgreSQL
- Redis
- Docker
- GitHub Actions

---

# Автор

Valeria Postylyakova
