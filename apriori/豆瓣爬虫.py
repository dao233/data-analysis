
#
#lists = csv.reader(open(file_name, 'r', encoding='utf-8-sig'))

import requests
import time
import csv
from selenium import webdriver

file_name = 'douban.csv'
out = open(file_name,'a', newline='', encoding='utf-8-sig')
csv_write = csv.writer(out, dialect='excel')
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
url = 'https://search.douban.com/movie/subject_search?cat=1002&search_text='

keyword = '张艺谋'

def download(keyword):
    browser = webdriver.Chrome()
    browser.get(url)
    input = browser.find_element_by_id('inp-query')
    input.send_keys(keyword)
    button = browser.find_element_by_xpath('//div[@class="inp-btn"]/input[@type="submit"]')
    button.click()

    films = browser.find_elements_by_xpath('//div[@class="title"]/a')
    actors = browser.find_elements_by_xpath('//div[@class="meta abstract_2"]')
    while len(films) >=15:
        temp = []
        for film in films:
            print(film.text)
        if len(films) == 16:
            films = films[1:]
            actors = actors[2:]
        for i in range(len(actors)):

            temp.append(films[i].text)
            for a in actors[i].text.split('/'):
                temp.append(a.strip())
            print(temp)
            csv_write.writerow(temp)
            temp = []
        
        next = browser.find_element_by_xpath('//a[@class="next"]')
        next.click()
        films = browser.find_elements_by_xpath('//div[@class="title"]/a')
        actors = browser.find_elements_by_xpath('//div[@class="meta abstract_2"]')

    browser.close()

download(keyword)