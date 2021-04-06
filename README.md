# Newspaper project

## Работа с почтой и выполнение задач по расписанию

- Для начала работы необходимо заполнить поля, относящиеся к почтовому серверу для отправки писем, в файле `NewsPaper/settings.py`:

```python
  EMAIL_HOST = ''

  EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = ''

  EMAIL_HOST_PASSWORD = ''

  EMAIL_PORT =

  EMAIL_USE_TLS =
```

- Для проверки входящих писем без использования реальных почтовых ящиков (для вывода их содержимого в консоль) нужно раскомментировать следующую строку в файле `NewsPaper/settings.py`

```python
  # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```