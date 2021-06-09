import scrapy, time

class MaerskSpider(scrapy.Spider):
   name = "maersktraining"
   allowed_domains = ["maersktraining.com"]
   start_urls = ["https://www.maersktraining.com/b2c-course-categories/"]

   def parse(self, response):
       for href in response.css(r"tr[style='h3'] ::attr(href)").extract():
           url = response.urljoin(href)
           print(url)
           req = scrapy.Request(url, callback=self.parse_titles)
           time.sleep(5)
           yield req

   def parse_titles(self, response):
       for sel in response.css('html').extract():
           data = {}
           data['title'] = response.css(r"h1[id='firstHeading'] i::text").extract()
           data['director'] = response.css(r"tr:contains('Directed by') a[href*='/wiki/']::text").extract()
           data['starring'] = response.css(r"tr:contains('Starring') a[href*='/wiki/']::text").extract()
           data['releasedate'] = response.css(r"tr:contains('Release date') li::text").extract()
           data['runtime'] = response.css(r"tr:contains('Running time') td::text").extract()
       yield data
