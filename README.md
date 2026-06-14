# Система учёта договоров

Веб-приложение для добавления, поиска и удаления договоров.

## Онлайн-версия (GitHub Pages)

После включения GitHub Pages приложение доступно по адресу:

**https://skrinleo.github.io/contract_system/**

Данные хранятся в `localStorage` браузера (без сервера).

### Как включить GitHub Pages

1. Откройте репозиторий на GitHub
2. **Settings** → **Pages**
3. **Build and deployment** → **Source**: `Deploy from a branch`
4. **Branch**: `main` → папка `/ (root)` → **Save**
5. Подождите 1–2 минуты и откройте ссылку выше

## Локальный запуск (FastAPI + SQLite)

```powershell
cd "C:\Users\H.Moran\Desktop\Qw\contract_system"
.\venv\Scripts\python.exe -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

Откройте: http://127.0.0.1:8000/

## Структура проекта

| Файл | Назначение |
|------|------------|
| `index.html` | Статическая версия для GitHub Pages |
| `static/app.js` | Логика приложения (localStorage) |
| `main.py`, `api.py` | Серверная версия (FastAPI) |
