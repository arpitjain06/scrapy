from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from amazon.items import AmazonItem


class MultipleSpider(CrawlSpider):
    name = "amazon"
    allowed_domains = ["amazon.com"]
    start_urls = ["http://www.amazon.com/Golf-Clothing/b/ref=sv_sv_so_sprtfit_0?ie=UTF8&node=2371053011"]
    #start_urls = ["http://www.amazon.com/s/ref=s9_acss_bw_cg_BeautCat_2a1?rh=i%3Abeauty%2Cn%3A11060711&ie=UTF8&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-3&pf_rd_r=0SXC8J9FCK1GSH0SGKQK&pf_rd_t=101&pf_rd_p=2392863802&pf_rd_i=11060451"]
  
    rules = (
        Rule(SgmlLinkExtractor(allow=(),), callback="parse_items", follow= True),
    )

    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.xpath('//li[contains(@class, "s-result-item  celwidget ")]/div[@class="s-item-container"]')
        items = []

        for site in sites:
            item = AmazonItem()
            item['description'] = site.xpath('div[@class="a-row a-spacing-mini"]/div[@class="a-row a-spacing-none"]/a/h2/text()').extract()
	    data = site.select('div[@class="a-row"]/a/span[contains(@class, "a-size-base a-color-price s-price a-text-bold")]/text()').extract()
	    if data:
            	item['discount_price'] = data
	    else:
		item['discount_price'] = site.xpath('div[@class="a-row a-spacing-mini"]/div[@class="a-row a-spacing-none"]/a/span[contains(@class, "a-size-base a-color-price s-price a-text-bold")]/text()').extract()
            #item['actual_price'] = site.select('div[@class="basic_stat product_score brief_metascore"]/div/div/span[contains(@class, "data metascore score")]/text()').extract()
            item['shipping_description'] = site.xpath('div[@class="a-row a-spacing-top-mini a-spacing-mini"]/div[@class="a-row a-spacing-none"]/span[contains(@class, "a-color-secondary")]/text()').extract()
	    brand = []
	    brand = site.xpath('div[@class="a-row a-spacing-mini"]/div[@class="a-row a-spacing-mini"]/span[@class="a-size-small a-color-secondary"]/text()').extract()
	    if brand:
            	item['brand'] = [brand[1]]

	    rating_data = site.xpath('div[@class="a-row a-spacing-none"]/span/span[@class="a-declarative"]/a/i[contains(@class, "a-icon a-icon-star a-star-4-5")]/span[contains(@class, "a-icon-alt")]/text()').extract()

	    data2=["None"]
	    if rating_data:
		item['rating'] = rating_data  
	    else:
		item['rating'] =data2

	    review_data = site.xpath('div[@class="a-row a-spacing-none"]/a[@class="a-size-small a-link-normal a-text-normal"]/text()').extract()
	    if review_data:           
		item['review'] =review_data
	    else:
		item['review'] =data2
            items.append(item)

        return items
