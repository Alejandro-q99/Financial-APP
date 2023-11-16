import scrapy
from finance_collector.items import BonosItem


class BonosSpider(scrapy.Spider):
    name = "bonos"
    allowed_domains = ["bonistas.com"]
    start_urls = ["https://bonistas.com/"]

    def parse(self, response):
        for row in response.xpath('//table/tbody/tr'):
            item = BonosItem()
            item['ticker'] = row.xpath('.//td[@id="ticker"]/a/text()').get()
            item['indice'] = row.xpath('.//td[2]/text()').get()
            item['precio'] = row.xpath('.//td[4]/span/text()').get()
            item['diferencia'] = row.xpath('.//td[5]/span/text()').get()
            item['tir'] = row.xpath('.//td[6]/text()').get()
            item['md'] = row.xpath('.//td[7]/text()').get()
            item['volumen'] = row.xpath('.//td[8]/text()').get()
            item['paridad'] = row.xpath('.//td[9]/text()').get()
            item['vt'] = row.xpath('.//td[10]/text()').get()
            item['ttir'] = row.xpath('.//td[11]/text()').get()
            item['uptir'] = row.xpath('.//td[12]/text()').get()
            item['dq'] = row.xpath('.//td[13]/span/text()').get()
            item['pq'] = row.xpath('.//td[14]/text()').get()
            item['qp'] = row.xpath('.//td[15]/span/text()').get()
            yield item
                
            