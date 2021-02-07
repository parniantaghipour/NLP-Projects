from __future__ import absolute_import
from scrapy.crawler import CrawlerProcess
import scrapy
import time
from imagecrawler.imagecrawler.items import ImagecrawlerItem


class HouzzSpider(scrapy.Spider):
    name = "houzz"
    size = 100
    count = 0

    def start_requests(self):
        urls = [
            'https://www.houzz.com/products/chairs',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # by using custom setting you do not need to five name of your file as input, the code will set it it self
    # comment this part (line 24) if you are not using the code paraller .
    custom_settings = {'FEED_URI': '%(category)s.csv', 'FEED_FORMAT': 'csv'}

    def parse(self, response):
        pro_urls = response.css(".hz-product-card a::attr(href)").extract()
        for url in pro_urls:
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_product)
            if url:
                self.count += 1
            if self.count >= self.size:
                # sleep to make sure the dada is saved
                time.sleep(2)
                return
        check_other_link = response.css('a.hz-pagination-link--next::attr(href)').get()
        # last_slash = check_other_link.split('/')[-1]
        # count = int(last_slash.split('?')[0])
        if check_other_link is not None:
            yield scrapy.Request(url=response.urljoin(check_other_link), callback=self.parse)

    def parse_product(self, response):
        # use item.py file to save items
        item = ImagecrawlerItem()
        item['name'] = response.css(".hz-view-product-title .view-product-title ::text").extract_first()
        imgs = response.css(".alt-images__thumb img::attr(src)").extract()[0:2]
        if imgs:
            try:
                item['image1'] = imgs[0].split('-w')[0].replace('_', '_9-').replace('fimgs', 'simgs')
                item['image2'] = imgs[1].split('-w')[0].replace('_', '_9-').replace('fimgs', 'simgs')
            except:
                print("No pic!")
        else:
            item['image1'] = response.css("img.view-product-image-print::attr(src)").get()

        item['summery'] = response.css("a.product-keywords .product-keywords__word::text").extract()
        yield item


# this part is needed for parallel usage of the code, if you uncomment this file without the input from the shell.
# if you want to add an item just make new process.crawl(HouzzSpider, category="?") then it will search it.
process = CrawlerProcess()

process.crawl(HouzzSpider, category="sofa")
process.crawl(HouzzSpider, category="desk")
process.start(stop_after_crawl=False)

process.stop()
