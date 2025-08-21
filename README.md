# Установка зависимостей
pip install -r requirements.txt

# Запуск скрипта
python main.py --file example1.log --report average

# Запуск скрипта с несколько файлов
python main.py --file example1.log example2.log --report average

# Запуск с фильтром по дате
python main.py --file example1.log --report average --date 2025-06-22

# Запуск тестов
pytest

# Запуск тестов с покрытием
pytest --cov=analyzer tests/