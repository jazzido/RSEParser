import re

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from resparser.items import ResparserItem


EMAIL_RE = re.compile(r"(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)",re.IGNORECASE)

class ResspiderSpider(CrawlSpider):
    domain_name = 'mapeo-rse.info'
    start_urls = ['http://www.mapeo-rse.info/promotores?tid[]=30&tid[]=26&tid[]=27']

    rules = (
        Rule(SgmlLinkExtractor(allow=(r'promotor/', )), 'parse_item', follow=True),
        Rule(SgmlLinkExtractor(allow=(r'promotores',))),
    )

    def parse_item(self, response):
        xs = HtmlXPathSelector(response)
        i = ResparserItem()
        l = XPathItemLoader(item=i, response=response)
        l.add_xpath('nombre_organizacion', '//h1[@class="title"]/text()')
        l.add_xpath('url_organizacion', '//div[@class="views-field-field-sitioweb-url"]/span/a/@href')
        l.add_xpath('email_organizacion', '//div[@class="views-field-field-correoinstitucional-email"]/span/a/text()')
        l.add_xpath('nombre_responsable', 
                    '//div[@class="views-field-field-personacontacto-nid"]//div[contains(@class, "node-type-personadecontacto")]/text()')
        l.add_xpath('email_responsable', '//div[@class="views-field-field-personacontacto-nid"]//*/text()', re=EMAIL_RE)
        
        return l.load_item()

SPIDER = ResspiderSpider()
