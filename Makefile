# Makefile для управления зависимостями, сборкой и публикацией с помощью Poetry

# Переменные
POETRY = poetry
PYTHON = python

# Цель по умолчанию
install:
	$(POETRY) install

# Цель для запуска brain-games
brain-games:
	$(POETRY) run brain-games

# Цель для запуска brain-games
brain-even:
	$(POETRY) run brain-even

# Цель для запуска brain-calc
brain-calc:
	$(POETRY) run brain-calc

# Цель для сборки пакета
build:
	$(POETRY) build

# Цель для тестовой публикации
publish-dry-run:
	$(POETRY) publish --dry-run

# Цель для установки собранного пакета
package-install:
	$(PYTHON) -m pip install --user dist/*.whl

# Цель для проверки flake8
lint:
	$(POETRY) run flake8 brain_games

