from bs4 import BeautifulSoup
import requests
import csv
from selenium import webdriver
import time
import json
driver = webdriver.Chrome(executable_path=r"F:\Desktop\Python Work\Parsing\chromedriver.exe")
contain_news_json = {}

try:
    driver.get(url=f"https://ru.investing.com/commodities/gold-news/0")
    driver = webdriver.Chrome(executable_path=r"F:\Desktop\Python Work\Parsing\chromedriver.exe")
    for it in range(1,100):
        driver.get(url=f"https://ru.investing.com/commodities/gold-news/{it}")
        with open(f"data/index.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
        
        with open(f"data/index.html", encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, "lxml")
        contain_news = soup.find_all("a", class_="title")
        data_news = soup.find_all("span", class_="date")
        
            
        for i in range(3, len(contain_news)):
                
            item_data = data_news[i-3].text.strip().replace(u"-\xa0", u"")
            item_news = contain_news[i].text.strip().replace(u"-\xa0", u"")
            try:
                contain_news_json[item_data] += f" {item_news}"   
            except Exception as ex:
                contain_news_json[item_data] = ""
                contain_news_json[item_data] += f" {item_news}"       
                    

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(contain_news_json , file, indent=4, ensure_ascii=False)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()