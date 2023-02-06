# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ExamplescrapyPipeline:
    def __init__(self):
        # Установка соединения с db и установка cursor
        self.con = sqlite3.connect('my_database.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        # Создание таблицы если она еще не создана
        self.cur.execute("""CREATE TABLE IF NOT EXISTS computers(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
        name TEXT, 
        core TEXT,
        cpu TEXT,
        ram TEXT,
        type_disk TEXT,
        capacity_disk TEXT,
        price TEXT
        )""")

    def process_item(self, item,spiderComputersSpider):
        # Запись данных в таблицу computers db 'my_database'
        data_tuple = (item['name'],item['core'],item['cpu'],item['ram'],item['type_disk'],item['capacity_disk'],item['price'])
        self.cur.execute ("""INSERT INTO computers(name, core, cpu, ram, type_disk, capacity_disk, price) VALUES (?,?,?,?,?,?,?);""", data_tuple) 
        self.con.commit()
        return item
