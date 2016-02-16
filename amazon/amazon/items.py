# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
class AmazonItem(Item):

    description = Field() # description of product
    discount_price = Field()  # price after discount
    #actual_price = Field() # price without discount
    shipping_description = Field() # shipping description of product  
    brand = Field()  # brand of product
    rating = Field()  # rating of product
    review = Field()  # review of product
