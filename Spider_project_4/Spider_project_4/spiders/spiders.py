import scrapy
from Spider_project_4.Spider_project_4.items import SpiderProject4Item
class DouBan(scrapy.Spider):
    name ="douban_book"#爬虫名字
    allowed_domain = ['douban.com']
    start_urls = "https://book.douban.com/top250"
    def parse_html(self,response):
        #解析第一页
        yield scrapy.Request(response.url,callback=self.parse_page())
        for page in response.path('//*[@id="content"]/div/div[1]/div/div/a'):
            link = page.xpath('@href').extract()[0]
            yield scrapy.Request(link,callback=page)
    def parse_page(self,response):
        for item in response.xpath('//tr[@class="item"]'):
            book = SpiderProject4Item()
            book['name'] = item.xpath('td[2]/div[1]/a@title').extract()[0]
            book['ratings'] = item.xpath('td[2]/div[2]/span[2]/span[@class=class="rating_nums"]/text()').extract()[0]
            book_info = item.xpath('td[2]/p[1]/text()').extract()[0]
            book_info_contents = book_info.srip().split('/')
            book['author'] = book_info_contents[0]
            book['publisher'] = book_info_contents[1]
            book['edition_year'] = book_info_contents[2]
            book['price'] = book_info_contents[3]
            yield book