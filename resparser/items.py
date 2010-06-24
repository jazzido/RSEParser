# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field
from scrapy.contrib.loader.processor import TakeFirst, MapCompose, Join
import string

class ResparserItem(Item):
    # define the fields for your item here like:
    # name = Field()
    nombre_organizacion = Field(
                              input_processor=MapCompose(string.strip),
                              output_processor=TakeFirst()
                          )
    nombre_responsable  = Field(
                              input_processor=MapCompose(string.strip),
                              output_processor=TakeFirst()
                          )
    email_organizacion  = Field(output_processor=TakeFirst())
    email_responsable   = Field(
                              input_processor=MapCompose(string.strip),
                              output_processor=Join(separator=u',')
                          )
    url_organizacion    = Field(output_processor=TakeFirst())

