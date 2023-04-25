before running tests:


[[_TOC_]]

## Task 1
### Переменные окружения
Перед запуском автотеста необходимо задать путь до конфиг-файла в виде переменной окружения
### macOS
```
export CONFIG='./task_1/configs/config.ini'
```
### Windows
```
set CONFIG='./task_1/configs/config.ini'
```
Запустить тест:
```
pytest -s -v task_1/tests/test_wiki_page_popularity_values.py
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