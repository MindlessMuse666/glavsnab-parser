import requests
from bs4 import BeautifulSoup, ResultSet, Tag
from model import Product
import json
import csv


def parser(url: str, max_item: int):
    create_json()
    create_csv()

    page: int = 1
    count_items: int = 0

    while max_item > count_items:
        products: list[Product] = []
        res = requests.get(url=f'{url}&p={page}')
        soup = BeautifulSoup(res.text, 'lxml')
        product_cards: ResultSet = soup.find_all('div', class_='product-card')

        for product in product_cards:
            if count_items >= max_item:
                break

            count_items += 1

            name: str = product.get('data-product-name')
            sku: str = product.find('span', class_='product-card__key').text

            pre_link_element: Tag = product.find('meta', itemprop='name')
            link: str = (pre_link_element
                         .findNext()
                         .get('href'))

            price_tag: Tag = product.find('span', itemprop='price')
            if price_tag:
                price: str = price_tag.get('content')
            else:
                price: str = 'По запросу'


            print(f'{count_items}-й товар\n' # Для отладки
                  f'Название: {name}\n'
                  f'Код: {sku}\n'
                  f'Ссылка на товар: {link}\n'
                  f'Цена за штуку: {price}\n')

            products.append(Product(
                sku=sku,
                name=name,
                link=link,
                price=price
            ))

        write_json(products)
        write_csv(products)
        page += 1


def create_json():
    open(file=f'glavsnab.json', mode='w', newline='')


def write_json(products: list[Product]):
    data: dict = {'product': []}

    for product in products:
        data['product'].append({
            'sku': product.sku,
            'name': product.name,
            'link': product.link,
            'price': product.price
        })

    with open(file=f'glavsnab.json', mode='a', newline='') as file:
        json.dump(obj=data, fp=file)


def create_csv():
    with open(file=f'glavsnab.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            'sku',
            'name',
            'link',
            'price'
        ])


def write_csv(products: list[Product]):
    with open(file=f'glavsnab.csv', mode='a', newline='') as file:
        writer = csv.writer(file)

        for product in products:
            writer.writerow([
                product.sku,
                product.name,
                product.link,
                product.price
            ])

if __name__ == '__main__':
    parser(url='https://glavsnab.net/zimniye-tovary.html?limit=100', max_item=672)