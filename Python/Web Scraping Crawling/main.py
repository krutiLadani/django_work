# coding=utf-8
"""This is the application for getting the trending items from kraftly website"""
import requests
from lxml import html
from db_config import DatabaseFunc

conn = DatabaseFunc()

html_page = requests.get('http://kraftly.com')  # get html from the given link
content = html.fromstring(html_page.content)  # convert the string to html content

items = content.xpath('//div[@class="desc"]/p/a/text()')  # gets all item names
price = content.xpath('//div[@class="prise"]/p[@class="price"]/text()')  # gets all item's price
category_shop = content.xpath('//p[@class="category-shop"]/a/text()')  # gets shop category of item
links = content.xpath('//div[@class="image"]/a/@href')  # get the links of each item

price_list = []
# trim the price list from white spaces, tabs and new lines
for p in price:
    pr = p.strip('\n\t\r ')
    if pr:
        price_list.append(pr)

for i, p, c, l in zip(items, price_list, category_shop, links):

    name = i.strip(' ')
    shop = c.strip(' ')

    item_page = requests.get(l)
    item_page_content = html.fromstring(item_page.content)
    desc = item_page_content.xpath('//p[@class="crossMd itemDesc sub_titl"]/text()')

    print "Name : " + name
    print "Price : " + p
    print "Shop : " + shop
    print "Details : " + desc[0]
    print "\n"

    records = {'name': name, 'price': p, 'cat_shop': shop, 'details': desc[0]}
    conn.insert_record(records)
