# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
from datetime import datetime


class AmazonPipeline(object):

	def __init__(self):
	    #self.conn = MySQLdb.connect("localhost", "root", "PWZAPp568lSlkwNN", "scrapy_database", charset="utf8", use_unicode=True) 
	    self.conn = MySQLdb.connect(user='root', passwd='PWZAPp568lSlkwNN', db='scrapy_database', host='localhost', charset="utf8", use_unicode=True)
	    #MySQLdb.connect(user='root', 'PWZAPp568lSlkwNN', 'scrapy_database', 'localhost', charset="utf8", use_unicode=True)
	    self.cursor = self.conn.cursor()	
  

	def process_item(self, item, spider): 
	     
	    try: 
		descrp = item.get('discount_price')
		if descrp[0]:
			descrp = descrp[0]
		else:
			descrp = None
		now = datetime.utcnow().replace(microsecond=0).isoformat(' ')
		self.cursor.execute("""INSERT INTO amazon_item (creation_date,discount_price, description, brand, review, rating, shipping_description) VALUES (%s,%s,%s,%s,%s,%s,%s)""" ,(now, item.get('discount_price')[0], item['description'][0],item['brand'][0], item.get('review')[0], item.get('rating')[0], item.get('shipping_description')[0]))
		self.conn.commit()


	    except MySQLdb.Error, e:
		print "#-----------------"
		print "Error  in %d: %s" % (e.args[0], e.args[1])


	    return item
