# LR_CI_CD

## Ruff
https://docs.astral.sh/ruff/linter/

```bash
ruff check --config=ruff.toml .\src\
```

## Pytest
https://docs.pytest.org/en/stable/index.html

```bash
pytest
```

## Задание
1. Сделать fork репозитория
2. Ознакомиться с функционалом Ruff
3. Написать Action(s), который при создании PR в master/main:
    - Будет прогонять Unit-Тесты и отказывать в слиянии, если не пройдет хотя бы 1 тест
    - Будет выводить  ошибки Ruff (например, с помощью https://github.com/astral-sh/ruff )

## Полезные ссылки
### Hooks
- [Туториал от Atlassian](https://www.atlassian.com/ru/git/tutorials/git-hooks)
- [Статья на Хабре](https://habr.com/ru/companies/2gis/articles/838966/)

### Actions
- [Документация GitHub Actions](https://docs.github.com/ru/actions)
- [Офф. Cheat-sheet GitHub](https://resources.github.com/actions/github-actions-cheat/)
- [Cheat-Sheet](Books/CI_CD/actions-cheat-sheet.pdf)
- [Статья на Хабре](https://habr.com/ru/companies/X5Tech/articles/651451/)
- [Какие типы триггеров (on) бывают](https://docs.github.com/ru/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows)

### Инструменты
- [Документация pytest](https://docs.pytest.org/en/stable/index.html)
- [Документация Ruff](https://docs.astral.sh/ruff/linter/)52
