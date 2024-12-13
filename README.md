# Парсер для сайта `glavsnab.net` (RU)

Этот проект представляет собой парсер для сайта `glavsnab.net`, разработанный для извлечения данных о товарах из категории "Зимние товары".  Парсер эффективно собирает информацию о товарах, обрабатывая необходимое количество страниц каталога. Результаты парсинга сохраняются в двух удобных форматах: `JSON` и `CSV`.

### Функциональность:

1. Извлечение данных о товарах из категории "Зимние товары" на сайте glavsnab.net. Обрабатывает все страницы пагинации.
2. Извлечение следующих данных для каждого товара:
    * `sku` (артикул товара)
    * `name` (название товара)
    * `link` (ссылка на страницу товара)
    * `price` (цена товара)  Если цена не указана на сайте, в поле записывается `"По запросу"`.
3. Поддержка форматов вывода `JSON` и `CSV`. Файлы сохраняются как `glavsnab.json` и `glavsnab.csv`.
4. Использование библиотеки `requests` для загрузки страниц и `BeautifulSoup` для парсинга `HTML`.
5. Структурирование данных с помощью dataclass для повышения читаемости и организации кода.

### Инструкция по использованию:

1. Установите необходимые библиотеки:
```shell
pip install requests beautifulsoup4
```
2. Запустите скрипт: `main.py`.
3. Результаты: Файлы `glavsnab.json` и `glavsnab.csv` будут созданы в той же директории, где находится скрипт.


---

# The parser for the `glavsnab.net` website (ENG)

This project is a parser for the `glavsnab.net` website, designed to extract product data from the "Winter goods" category. The parser efficiently collects product information, processing up to 672 pages of the catalog. Parsing results are saved in two convenient formats: `JSON` and `CSV`.

### Functionality:

1. Extraction of product data from the "Winter goods" category on the glavsnab.net website. Processes all pagination pages.
2. Extraction of the following data for each product:
    * sku (product SKU)
    * name (product name)
    * link (link to the product page)
    * price (product price) If the price is not specified on the website, "On request" is written to the field.
3. Support for JSON and CSV output formats. Files are saved as glavsnab.json and glavsnab.csv.
4. Uses the requests library for downloading pages and BeautifulSoup for parsing HTML.
5. Data structuring using dataclass for improved readability and code organization.

### Usage Instructions:

1. Install necessary libraries:
```shell
pip install requests beautifulsoup4
```
2. Run the script: `main.py`.
3. Results: The `glavsnab.json` and `glavsnab.csv` files will be created in the same directory as the script.
