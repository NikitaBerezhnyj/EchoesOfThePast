# Contributing

This file is available in both [Ukrainian](#внесок-ukraine) and [English](#contribution-uk).

## Внесок :ukraine:

Дякуємо за ваш інтерес до участі в розвитку проекту! Ми цінуємо ваш внесок, незалежно від того, чи це буде код, документація, або обговорення ідей.

### Як ви можете допомогти?

#### 1. Повідомлення про проблеми

Якщо ви виявили помилку, маєте пропозицію щодо покращення або знайшли неточність у документації, створіть **Issue** у цьому репозиторії. Будь ласка, переконайтеся, що ви надали наступну інформацію:

- Чіткий опис проблеми
- Кроки для відтворення помилки (якщо це помилка)
- Пропозиції щодо вирішення (за бажанням)

#### 2. Додавання нового функціоналу

Якщо ви хочете додати новий функціонал:

- Спершу обговоріть вашу ідею, створивши **Issue**
- Після отримання згоди від мейнтейнерів, створіть **Pull Request** з вашими змінами

#### 3. Редагування документації

Допомога з покращенням чи розширенням документації завжди вітається! Ви можете редагувати файл `README.md` або додавати нові документи за потреби.

#### 4. Перегляд Pull Request'ів

Якщо у вас є досвід і знання, ви можете переглядати відкриті Pull Request'и та залишати коментарі чи пропозиції.

### Процес внесення змін

#### 1. Форк репозиторію

Натисніть **Fork** у верхній частині сторінки, щоб створити копію репозиторію у вашому акаунті.

#### 2. Клонування проєкту

Склонуйте форк у вашу локальну машину:

```bash
git clone https://github.com/your-username/EchoseOfThePast.git
```

#### 3. Створення нової гілки

Перед внесенням змін створіть нову гілку:

```bash
git checkout -b feature/your-feature-name
```

#### 4. Внесення змін

Внесіть ваші зміни в код або документацію.

#### 5. Тестування змін

Переконайтеся, що ваші зміни пройшли всі необхідні тести. Якщо тестів немає, додайте їх, якщо це доречно.

#### 6. Створення Pull Request

Після завершення змін створіть Pull Request. У описі Pull Request поясніть, які зміни були внесені та чому.

## Формат повідомлень комітів

Для покращення читабельності історії комітів і спрощення співпраці в команді, ми дотримуємося стандарту форматування повідомлень комітів, заснованого на **Conventional Commits**.

**Формат:**

```bash
git commit -m "<type>: <message>"
```

Де:

- `<type>` — тип зміни (наприклад, `feat`, `fix`, `chore`, `docs`).
- `<message>` — короткий опис змін.

**Приклади:**

- `feat: додано нову функціональність для обробки замовлень`
- `fix: виправлено помилку при реєстрації користувача`
- `chore: оновлено залежності`
- `docs: оновлено інструкції по запуску проекту`

**Типи комітів:**

- `feat`: нові функції.
- `fix`: виправлення помилок.
- `chore`: зміни, які не впливають на бізнес-логіку (наприклад, оновлення залежностей).
- `docs`: зміни в документації.
- `refactor`: рефакторинг коду (зміни, що не виправляють помилки і не додають нових функцій).
- `test`: додавання або оновлення тестів.

Будь ласка, дотримуйтеся цього формату при створенні комітів.

---

## Contribution :uk:

Thank you for your interest in contributing to the project! We appreciate your input, whether it's code, documentation, or sharing ideas.

### How Can You Help?

#### 1. Reporting Issues

If you’ve found a bug, have a suggestion for improvement, or spotted an inaccuracy in the documentation, please create an **Issue** in this repository. Make sure to provide the following information:

- A clear description of the issue
- Steps to reproduce the error (if it’s a bug)
- Suggestions for resolution (optional)

#### 2. Adding New Features

If you want to add a new feature:

- First, discuss your idea by opening an **Issue**
- Once you get approval from the maintainers, create a **Pull Request** with your changes

#### 3. Editing Documentation

Contributions that improve or expand the documentation are always welcome! You can edit the `README.md` file or add new documents as needed.

#### 4. Reviewing Pull Requests

If you have experience and knowledge, feel free to review open Pull Requests and leave comments or suggestions.

### Contribution Workflow

#### 1. Fork the Repository

Click **Fork** at the top of the page to create a copy of the repository in your account.

#### 2. Clone the Project

Clone the fork to your local machine:

```bash
git clone https://github.com/your-username/EchoseOfThePast.git
```

#### 3. Create a New Branch

Before making any changes, create a new branch:

```bash
git checkout -b feature/your-feature-name
```

#### 4. Make Changes

Apply your changes to the code or documentation.

#### 5. Test Your Changes

Ensure your changes pass all necessary tests. If there are no tests, consider adding them if appropriate.

#### 6. Create a Pull Request

Once your changes are complete, create a Pull Request. In the PR description, explain what changes you made and why.

## Commit Message Format

To improve commit history readability and simplify collaboration, we follow the **Conventional Commits** standard.

**Format:**

```bash
git commit -m "<type>: <message>"
```

Where:

- `<type>` — the type of change (e.g., `feat`, `fix`, `chore`, `docs`).
- `<message>` — a short description of the change.

**Examples:**

- `feat: added new feature for order processing`
- `fix: resolved user registration bug`
- `chore: updated dependencies`
- `docs: updated project launch instructions`

**Commit Types:**

- `feat`: new features.
- `fix`: bug fixes.
- `chore`: changes that don’t affect business logic (e.g., dependency updates).
- `docs`: documentation updates.
- `refactor`: code refactoring (not fixing bugs or adding features).
- `test`: adding or updating tests.

Please follow this format when creating commits.
