from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import element
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pprint import pprint
import time
import asyncio
import bs4
import json

@asyncio.coroutine
def driverGet():
    chromeOptions = Options()
    chromeOptions.add_argument('headless')
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get('https://www.rocketpunch.com/jobs?job=sw-developer')

    while True:
        if driver.page_source[-7:] == "</html>":
            print('page loaded')
            time.sleep(0.0001)
            items = BeautifulSoup(driver.page_source, 'html.parser').find_all(attrs={'class':'company item'})    
            if  items != []:
                print('items ready')
                break

        yield from asyncio.sleep(0.5)

    # companies = []
        # company = {}
            # company['name'] = ''
            # company['sector'] = ''
            # company['jobs'] = [] 
                # job = {}
                    # job['title'] = ''
                    # job['career'] = ''
                    # job['link'] = ''
                    # job['valid_until'] = ''
                    # job['modified'] = ''


    companies = []
    for item in items:
        name = item.find(attrs={'class': 'header name'}) \
            .find(lambda x : 
                not isinstance(x, element.NavigableString)
                and x.name == 'strong').text
        sector = item.find(attrs={'class': 'nowrap meta'}).get_text().strip()

        company = {}
        company['name'] = name # 회사명
        company['sector'] = sector # 업종

        jobs = []
        company['jobs'] = jobs # 채용

        for desc in item.find_all(attrs={'class': 'job-detail'}):
            if not isinstance(desc, element.NavigableString) and 'job-detail' in desc.get_attribute_list('class'):
                job = {}
                job['title'] = desc.find(attrs={'class': 'job-title'}).text
                job['career'] = desc.find(attrs={'class': 'job-stat-info'}).text
                job['link'] = desc.a['href']
                job and jobs.append(job)

        companies.append(company)
        pprint(company)

        driver.quit()

    json_data = json.dumps(companies, ensure_ascii=False)
    with open('.\\companies.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False)
    # pprint(companies)
    pprint(companies)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(driverGet())

if __name__ == '__main__':
    main()