import scrapy
import csv
import re
from bs4 import BeautifulSoup
from lxml import etree
from gsmSpider.items import GsmspiderItem


class GsmSpider(scrapy.Spider):
    name = 'gsm'
    allowed_domains = ['www.ncbi.nlm.nih.gov']
    start_urls = ['https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM2876451']
    url_head = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc='

    def start_requests(self):
        data = []
        plat = []
        gses = []
        exp = []
        with open(r'C:\Users\QiTianM425\Desktop\test1.csv', 'r', encoding='UTF-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                data.append(row[0])
                plat.append(row[1])
                gses.append(row[2])
                exp.append(row[3])
        n = 0
        for i in data:
            url = self.url_head + str(i)
            item = GsmspiderItem()
            item["GSM_num"] = i
            item["Platform"] = plat[n]
            item["GSE_num"] = gses[n]
            item["ExpType"] = exp[n]
            n = n+1
            yield scrapy.Request(url=url, meta={'item': item}, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        cont = soup.find_all("tr", valign="top")
        bot = len(cont)
        pat1 = 'Status'
        pat2 = 'Source name'
        pat3 = 'Organism'
        pat4 = 'Characteristics'
        pat5 = 'Extracted molecule'
        for i in range(0, bot):
            A = re.search(pat1, str(cont[i]))
            B = re.search(pat2, str(cont[i]))
            C = re.search(pat3, str(cont[i]))
            D = re.search(pat4, str(cont[i]))
            E = re.search(pat5, str(cont[i]))
            if A:
                html = etree.HTML(str(cont[i]))
                Status = html.xpath('//tr[@valign = "top"]/td[position()=2]/text()')[0]
            if B:
                html = etree.HTML(str(cont[i]))
                Source_name = html.xpath('//tr[@valign = "top"]/td[position()=2]/text()')[0]
            if C:
                html = etree.HTML(str(cont[i]))
                organism = html.xpath('//tr[@valign = "top"]/td[position()=2]/a/text()')
                org = ', '.join(organism)
            if D:
                html = etree.HTML(str(cont[i]))
                character = html.xpath('//tr[@valign = "top"]/td[position()=2]/text()')
                cha = ', '.join(character)
            if E:
                html = etree.HTML(str(cont[i]))
                Extracted = html.xpath('//tr[@valign = "top"]/td[position()=2]/text()')[0]

        item = response.meta['item']
        item["Status"] = Status
        item["Source_name"] = Source_name
        item["Organism"] = org
        item["Characteristics"] = cha
        item["Extracted_molecule"] = Extracted
        yield item
