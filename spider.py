import scrapy

class BlogSpider(scrapy.Spider):
    name = 'uuspider'
    start_urls = ['http://pauuu.cn/nr.php?id=0']
    selector = (
        'body > div.details.clearfix > div >'
        'div.d-left > div.matter01.mb > div.introduce'
        ' > div.video-h.pl > h3'
    )
    def parse(self, response):
        for title in response.css(self.selector):
            result = title.css('h3 ::text').get()
            if result == "" or not result:
                continue
            yield {'title': result}

        for id in range(350, 465):
            yield response.follow(f'http://pauuu.cn/nr.php?id={id}', self.parse)