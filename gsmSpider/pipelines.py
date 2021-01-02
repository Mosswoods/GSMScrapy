# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import pymysql

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GsmspiderPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host="localhost", user="root", password="goodxyl2021", db="webdesign")
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        GSM = item["GSM_num"]
        Status = item["Status"]
        Source_name = item["Source_name"]
        Organism = item["Organism"]
        Characteristics = item["Characteristics"]
        Extracted_molecule = item["Extracted_molecule"]
        Platform = item["Platform"]
        GSE = item["GSE_num"]
        EXP = item["ExpType"]
        self.cursor.execute(
            'insert into gsm(GSM_num, Status, Source_name, Organism, Characteristics, Extracted_molecule, Platform, GSE_num, Experiment_type) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (
                GSM, Status, Source_name, Organism, Characteristics, Extracted_molecule, Platform, GSE, EXP))
        self.connect.commit()

        # with open(r"C:\Users\QiTianM425\Desktop\result.csv", 'a+', encoding='utf-8', newline="") as cf:
        #     w = csv.writer(cf)
        #     w.writerow([GSM, Status, Source_name, Organism, Characteristics, Extracted_molecule, Platform])
        # return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
