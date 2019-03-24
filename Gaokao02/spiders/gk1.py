import scrapy

class gaokao(scrapy.Spider):
    name = "gk1"
    def start_requests(self):
        urls = [
            'https://gkcx.eol.cn/schoolhtm/schoolAreaPoint/31/10003/10035/10036.htm'
        ]
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        # /html/body/div[9]/div/div[2]/div[4]
        xinxi1 = response.xpath("//div[@class='places-tab margin20']")
        xinxi2=xinxi1.xpath("//tbody//tr")
        # print(xinxi2)
        for xinxi3 in xinxi2:
            # print(xinxi3)
            xinxi4=xinxi3.css('td::text')
            year =  xinxi4[0]
            print(year)
            max = xinxi4[1]
            min = xinxi4[3]
            # with open('test1.html', 'w+') as wf:
            #     wf.write(xinxi4)



