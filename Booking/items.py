# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class BookingItem(Item):  
    State=Field()
    Country=Field()
    Hotel_ID=Field()
    Hotel_Name=Field()
    City = Field()
    pass

    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
