# -*- coding: utf-8 -*-
from PicGet.items import PicgetItem
from scrapy.selector import Selector
import scrapy
from scrapy.contrib.loader import ItemLoader, Identity

class DoutuSpider(scrapy.Spider):
    name = "Doutu"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = []
    def start_requests(self):
        file_opened = open('TBid.txt','r')
        try:
            url_head = 'http://www.tieba.baidu.com/p/'
            for line in file_opened:
                self.start_urls.append(url_head + line + "?pn=1")
            for url in self.start_urls:
                yield scrapy.Request(url, callback=self.parse)
        finally:
            file_opened.close()

    def parse(self, response):
        sel = Selector(response)
        pagenum = sel.xpath("//span[@class = 'red']/text()").extract()
        if len(pagenum)>0:
            for i in range(1,int(pagenum[-1])+1):
                link = response.url[:-1]+str(i)
                request = scrapy.Request(link, callback=self.parse_item)
                yield request

    def parse_item(self,response):
        item = ItemLoader(item=PicgetItem(),response = response)
        item.add_xpath('image_urls',"//img[@class = 'BDE_Image']/@src",Identity())
        item.add_value('url',response.url)
        return item.load_item()