### Переменные окружения
Перед запуском автотестов необходимо задать путь до конфиг-файла в виде переменной окружения
### macOS/Linux
```
export CONFIG='./task_1/configs/config.ini'
```
### Windows
```
set CONFIG='./task_1/configs/config.ini'
```

### Установка зависимостей с Pipenv
Необходимо выполнить следующие команды из корневой директории проекта:

* установить pipenv
```bash
pip3 install pipenv
```
* инициализировать проект и установить зависимости
```bash
pipenv install
```
* активировать окружение проекта
```
pipenv shell
```
## Task 1
Запустить тест:
```
pytest -s -v task_1/tests/test_wiki_page_popularity_values.py
```

## Task 2
Запустить тесты:
```
pytest -s -v task_2/tests
```
