## Опис

Цей проєкт містить автоматизовані тести для перевірки функціональності пошуку в Google за допомогою бібліотеки Selenium на Python. Тести перевіряють різні сценарії використання Google, такі як пошук за ключовими словами, автодоповнення, фільтри вкладок, фільтри часу, специфічні пошукові запити тощо.

### Вимоги

-	Python 3.8 або вище
-	Google Chrome (остання версія)
-	Установлений пакет Selenium

### Установка

Встановити необхідні залежності:
```bash
pip install selenium
```

## Виконання тестів

Запустіть файл із тестами за допомогою Python:
```bash
python test_google_search.py
```

### Сценарії тестів

1.	**Пошук за ключовим словом**: Тест перевіряє функціональність пошуку за конкретним ключовим словом (“Flask documentation”). Після введення запиту, тест перевіряє, чи є результати пошуку, які містять це ключове слово.
2.	**Пошук за кількома ключовими словами**: Тест перевіряє пошук за кількома ключовими словами (“Python tutorial Django tutorial”) і перевіряє, чи є на сторінці результати, які містять кожне з цих слів, незалежно від регістру.
3.	**Фільтри вкладок**: Тест перевіряє, чи доступні вкладки пошуку, такі як “Новини”, “Зображення” та “Відео” після того, як був здійснений пошук за ключовим словом (“Django tutorials”).
4.	**Пошук за доменом**: Тест перевіряє використання оператора site: для пошуку на певному домені (наприклад, site:github.com Django). Тест перевіряє, чи всі результати пошуку належать до цього домену.
5.	**Пошук за заголовком**: Тест використовує оператор intitle: для пошуку за конкретним словом у заголовку сторінок. Тест перевіряє, чи містять результати заголовки, що включають слово “Flask”.
6.	**Пошук зображень**: Тест перевіряє функціональність пошуку за зображеннями. Він здійснює пошук за ключовим словом “sunset” на вкладці “Зображення” і перевіряє, чи з’являються зображення на сторінці результатів.