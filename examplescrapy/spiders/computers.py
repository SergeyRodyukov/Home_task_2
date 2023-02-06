import scrapy
from scrapy.spiders import Spider
import re

class ComputersSpider(Spider):

    name = 'computers'
    allowed_domains = ['notik.ru']
    

    default_headers = {}
    def scrap_computers(self, response):
        page_id = 0 # счетчик для отлова имени ноутбука
        
        all_cards = response.xpath("//tr[@class='goods-list-table']")  # все карточки ноутбуков
        for card in all_cards:
            count = 0    
            performance = card.xpath(".//td[@class='glt-cell w4']") # характеристика текущего ноутбука

            name = response.xpath(".//tr[@class='hide-mob']//b")[page_id].css('::text').get() # его имя
            page_id += 1

            for i in performance:
                count += 1
                if count == 1 :
                    core = i.css("::text")[1].get()
                    cpu = re.findall(r'\d+', i.css("::text")[5].get())
                    cpu = str("".join(cpu))
                elif count == 2 :
                    ram = i.css("::text")[0].get()
                    type_disk = i.css("::text")[4].get()
                    capacity_disk = re.findall(r'\d+\s[Г][Б]',i.css("::text")[6].get())
                    capacity_disk = str("".join(capacity_disk))
                    break
            price_selector = card.xpath(".//td[@class='glt-cell gltc-cart']")
            price = re.findall(r'\d+', price_selector.xpath(".//b").css("::text").get())
            price = str("".join(price))

            # запись результатов поиска в словарь
            item = {}
            item['name'] = name
            item['core'] = core
            item['cpu'] = cpu
            item['ram'] = ram
            item['type_disk'] = type_disk
            item['capacity_disk'] = capacity_disk
            item['price'] = price

            # возвращаем словарь для записи в db
            yield item

    def start_requests (self):
        
        # список страница для прохода
        for page in range(1,3):
            url = f'https://www.notik.ru/search_catalog/filter/work.htm?page={page}'
            yield scrapy. Request (url, callback=self.scrap_computers)





 