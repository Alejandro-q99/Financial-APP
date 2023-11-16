# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class BonosItem(scrapy.Item):
    ticker = scrapy.Field()
    indice = scrapy.Field()
    precio = scrapy.Field()
    diferencia = scrapy.Field()
    tir = scrapy.Field()
    md = scrapy.Field()
    volumen = scrapy.Field()
    paridad = scrapy.Field()
    vt = scrapy.Field()
    ttir = scrapy.Field()
    uptir = scrapy.Field()
    dq = scrapy.Field()
    pq = scrapy.Field()
    qp = scrapy.Field()
