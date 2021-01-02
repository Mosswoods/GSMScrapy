# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GsmspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GSM_num = scrapy.Field()
    Status = scrapy.Field()
    Source_name = scrapy.Field()
    Organism = scrapy.Field()
    Characteristics = scrapy.Field()
    Extracted_molecule = scrapy.Field()
    Platform = scrapy.Field()
    GSE_num = scrapy.Field()
    ExpType = scrapy.Field()


