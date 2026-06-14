# Система учёта договоров

Веб-приложение для добавления, поиска и удаления договоров.

## Онлайн-версия (GitHub Pages)

Данные хранятся в `localStorage` браузера (без сервера).

## Локальный запуск (FastAPI + SQLite)

```powershell
cd "C:\User\contract_system"
.\venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Откройте: http://127.0.0.1:8000/

## Структура проекта

| Файл | Назначение |
|------|------------|
| `index.html` | Статическая версия для GitHub Pages |
| `static/app.js` | Логика приложения (localStorage) |
| `main.py`, `api.py` | Серверная версия (FastAPI) |
