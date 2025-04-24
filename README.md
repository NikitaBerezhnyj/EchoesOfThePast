# Echoes Of The Past

This project is available in: [Ukrainian :ukraine:](#echoes-of-the-past-ukraine) and [English :uk:](#echoes-of-the-past-uk)

## Echoes Of The Past :ukraine:

**Відлуння минулого** — це психологічна драма у жанрі візуальної новели, що занурює гравця у таємничий світ підземної таверни, створеної лише для тих, хто перебуває у психологічній кризі. Гра досліджує теми внутрішньої порожнечі, втечі від реальності та вибору між ілюзією комфорту і болісною правдою.

### Про проєкт

Гра розроблена на рушії Ren'Py та доступна для платформ Windows, macOS, Linux, а також має мобільну та веб-версії. Унікальний візуальний стиль, глибокий сюжет та атмосферний звуковий супровід створюють занурювальний досвід, де кожне рішення гравця впливає на розвиток історії та визначає кінцівку.

#### Особливості

- **Нелінійний сюжет** з декількома різними кінцівками
- **Динамічний внутрішній монолог** головного героя, що змінюється залежно від вибору гравця
- **Психологічно глибокі персонажі** з власними історіями та мотивами
- **Гіпнотична атмосфера** таверни, що змінюється відповідно до емоційного стану героя
- **Атмосферний аудіо-дизайн**, що підсилює психологічну глибину історії

### Встановлення

```bash
# Клонувати репозиторій
git clone https://github.com/NikitaBerezhnyj/EchoesOfThePast.git

# Перейти в директорію проєкту
cd EchoesOfThePast

# Запустити гру за допомогою Ren'Py launcher
```

### Розробка

Проєкт використовує рушій Ren'Py 8.2.0 або новіший. Для участі в розробці потрібно:

1. Встановити [Ren'Py](https://www.renpy.org/latest.html)
2. Клонувати репозиторій
3. Відкрити проєкт у Ren'Py Launcher

#### Структура проєкту

```
EchoesOfThePast/
│
├── game/
│   ├── audio/                      # Аудіо файли
│   │   ├── music/                  # Фонова музика
│   │   └── sounds/                 # Звукові ефекти
│   |
│   ├── fonts/                      # Шрифти
│   ├── gui/                        # Файли інтерфейсу користувача
│   ├── images/                     # Зображення та графіка
│   │   ├── art/                    # Ілюстрації
│   │   ├── backgrounds/            # Фони
│   │   └── characters/             # Персонажі
│   │
│   ├── gui.rpy                     # Налаштування графічного інтерфейсу
│   ├── options.rpy                 # Налаштування гри
│   ├── screens.rpy                 # Екрани інтерфейсу
│   └── script.rpy                  # Основний скрипт гри
│
├── drafts/                         # Робочі файли (.psd, .kra, .fpl, тощо)
│
├── docs/                           # Документація
│   ├── 01_game_design.md           # Загальний опис гри
│   ├── 02_narrative.md             # Сюжет, персонажі, вибори
│   ├── 03_visual_guide.md          # Візуальний стиль
│   ├── 04_audio_guide.md           # Аудіо оформлення
│   └── 05_technical_details.md     # Технічні деталі
│
├── LICENSE                         # Ліцензія проєкту
├── CONTRIBUTING.md                 # Правила внесення внесків для сторонніх розробників
├── CODE_OF_CONDUCT.md              # Кодекс поведінки учасників
├── SECURITY.md                     # Політика безпеки
├── TODO.md                         # Список завдань
└── README.md                       # Цей файл
```

### Задачі

Список поточних завдань, над якими працює команда, можна знайти в файлі [TODO.md](./TODO.md). Якщо ви хочете долучитися до розробки, перегляньте цей файл для ознайомлення з актуальними потребами проєкту.

### Документація

Уся проєктна документація структурована у п’ять ключових файлів:

- [01_game_design.md](./docs/01_game_design.md) — загальна концепція гри та її механіки
- [02_narrative.md](./docs/02_narrative.md) — сюжетна структура, персонажі та варіанти вибору
- [03_visual_guide.md](./docs/03_visual_guide.md) — візуальний стиль і напрям дизайну
- [04_audio_guide.md](./docs/04_audio_guide.md) — принципи звукового оформлення
- [05_technical_details.md](./docs/05_technical_details.md) — технічні аспекти розробки

Ці файли містять усю необхідну інформацію для глибокого розуміння структури гри та участі в її розвитку.

### Робота з графічними та аудіо файлами

Всі робочі файли (.psd, .krita, .fpl та інші) слід зберігати в директорії `drafts/`. Кінцеві оптимізовані файли для використання в грі мають зберігатись у відповідних директоріях в `game/`.

### Внесок

Ми радо вітаємо внески в проєкт! Будь ласка, ознайомтеся з [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) перед тим, як долучитися до розробки.

Процес внесення змін описаний в файлі [CONTRIBUTING.md](./CONTRIBUTING.md)

### Ліцензія

Цей проєкт поширюється під ліцензією [назва ліцензії]. Детальніше в файлі [LICENSE](./LICENSE).

---

## Echoes Of The Past :uk:

**Echoes Of The Past** is a psychological drama visual novel that immerses the player in the mysterious world of an underground tavern, created solely for those undergoing a psychological crisis. The game explores themes of inner emptiness, escapism, and the choice between the illusion of comfort and the painful truth.

### About the Project

The game is developed using the Ren'Py engine and is available for Windows, macOS, and Linux, with both mobile and web versions. A unique visual style, deep narrative, and atmospheric audio design create an immersive experience where every decision the player makes affects the story's progression and determines the ending.

#### Features

- **Non-linear narrative** with multiple possible endings
- **Dynamic inner monologue** of the protagonist, which changes based on player choices
- **Psychologically complex characters** with their own stories and motivations
- **Hypnotic tavern atmosphere** that evolves with the emotional state of the protagonist
- **Atmospheric audio design** that deepens the psychological impact of the story

### Installation

```bash
# Clone the repository
git clone https://github.com/NikitaBerezhnyj/EchoesOfThePast.git

# Navigate to the project directory
cd EchoesOfThePast

# Launch the game via the Ren'Py launcher
```

### Development

The project uses Ren'Py version 8.2.0 or newer. To participate in development:

1. Install [Ren'Py](https://www.renpy.org/latest.html)
2. Clone the repository
3. Open the project using the Ren'Py Launcher

#### Project Structure

```
EchoesOfThePast/
│
├── game/
│   ├── audio/                      # Audio files
│   │   ├── music/                  # Background music
│   │   └── sounds/                 # Sound effects
│   │
│   ├── fonts/                      # Fonts
│   ├── gui/                        # User interface files
│   ├── images/                     # Images and artwork
│   │   ├── art/                    # Illustrations
│   │   ├── backgrounds/            # Backgrounds
│   │   └── characters/             # Characters
│   │
│   ├── gui.rpy                     # GUI configuration
│   ├── options.rpy                 # Game settings
│   ├── screens.rpy                 # Interface screens
│   └── script.rpy                  # Main game script
│
├── drafts/                         # Source/working files (.psd, .kra, .fpl, etc.)
│
├── docs/                           # Documentation
│   ├── 01_game_design.md           # General game design overview
│   ├── 02_narrative.md             # Story, characters, choices
│   ├── 03_visual_guide.md          # Visual style guide
│   ├── 04_audio_guide.md           # Audio design guide
│   └── 05_technical_details.md     # Technical details
│
├── LICENSE                         # Project license
├── CONTRIBUTING.md                 # Contribution guidelines
├── CODE_OF_CONDUCT.md              # Code of conduct for contributors
├── SECURITY.md                     # Security policy
├── TODO.md                         # Task list
└── README.md                       # This file
```

### Tasks

The list of current development tasks can be found in the [TODO.md](./TODO.md) file. If you would like to contribute to the project, please check this file for up-to-date development needs.

### Documentation

All project documentation is organized into five key files:

- [01_game_design.md](./docs/01_game_design.md) — general concept and mechanics of the game
- [02_narrative.md](./docs/02_narrative.md) — narrative structure, characters, and choices
- [03_visual_guide.md](./docs/03_visual_guide.md) — visual direction and design principles
- [04_audio_guide.md](./docs/04_audio_guide.md) — audio design principles
- [05_technical_details.md](./docs/05_technical_details.md) — technical aspects of development

These files contain all the necessary information for understanding the game structure and participating in development.

### Working with Graphics and Audio Files

All editable source files (.psd, .krita, .fpl, and others) should be stored in the `drafts/` directory. Final optimized files for use in the game should be placed in the appropriate subdirectories within `game/`.

### Contributions

We welcome contributions to the project! Please review [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) before getting involved.

The contribution process is described in [CONTRIBUTING.md](./CONTRIBUTING.md)

### License

This project is licensed under [license name]. See the [LICENSE](./LICENSE) file for more information.
