# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field 

class ExamplescrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # Поля для таблицы db с насследование от класса Field
    name = Field()
    cpu = Field()
    core = Field()
    ram = Field()
    type_disk = Field()
    capacity_disk = Field()
    price = Field()


