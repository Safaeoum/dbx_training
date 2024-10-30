## Pre-requisites

- Python 3.10.X
- Poetry 1.8.4

## Getting Started

0. Set venv in project

```
Potery config --list
```

```
poetry config virtualenvs.in-project true
```

1. `poetry env use 3.10`
2. 
poetry run python --version
// or 
poetry shell
python --version

3.

```
poetry run python -m src.training_objets_trouves.main
```

```
poetry run pytest
```

```
poetry build
```

```
poetry run ruff check --fix
```

```
poetry run task_main
```
