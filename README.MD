# Newspaper (DB test)
Для создания и теста базы данных выполнить команды:

```
python manage.py migrate
python manage.py shell < commands.py
```

Результаты тестирования будут выведены в файл `stats.txt`.

Модель `Author` находится в приложении `accounts`.  
Модели `Category`, `Post` и `Comment` расположены в приложении `news`.

---

### ЗАМЕТКИ ДЛЯ МЕНТОРА

1\. Изначально пробовал реализовать задание, импортируя в оба модуля модель `User` и делая в модуле `news` импорт модели `Author` (т.к. она используется в модели `Post`),

```python
# [news/models.py]
from django.contrib.auth.models import User
from accounts.models import Author
```

а в модуле `accounts` импорт моделей `Post` и `Comment` (т.к. они используются в методе `update_rating`),

```python
# [accounts/models.py]
from django.contrib.auth.models import User
from news.models import Post, Comment
```

но, конечно, получил ошибку `circular import`.

2\. Тогда попробовал в модуле `accounts` вместо импорта использовать внутри метода получение необходимых моделей с помощью `apps.get_model`.

```python
# [accounts/models.py]
# ...
class Author(models.Model):
# ...
    def update_rating(self):
        Post = apps.get_model('news.Post')
        Comment = apps.get_model('news.Comment')
```

После этого всё заработало, как предполагалось.

3\. И, наконец, задался вопросом, можно ли вообще обойтись без очевидных импортов моделей, т.е. через `from ... import ... `, из одних приложений в другие, и оказалось, что можно. В полях моделей, которые используются для связей с другими моделями, типа `ForeignKey` или `OneToOneField`, стал использовать названия моделей в кавычках, предваряя их названием приложения, и вроде бы всё работает.

```python
# [news/models.py]
# ...
class Post(models.Model):
    author = models.ForeignKey('accounts.Author', on_delete=models.CASCADE)
# ...
class Comment(models.Model):
    # ...
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
```

```python
# [accounts/models.py]
# ...
class Author(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
```

4\. В итоге, до конца не уверен, всё ли учёл, но надеюсь, что это не самый неправильный способ связи моделей из разных приложений.
