# Makefile для управления установкой зависимостей с помощью Poetry

# Цель по умолчанию
install:
	poetry install

# Цель для запуска brain-games
brain-games:
	$(POETRY) run brain-games

# Определение переменных (опционально)
POETRY = poetry

# Использование переменной для установки
install_with_var:
	$(POETRY) install