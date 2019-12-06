import os
os.system('cls')
from selenium import webdriver
from bs4 import BeautifulSoup
# from bs4 import element as ele
from bs4 import element
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pprint import pprint

chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("headless")
driver = webdriver.Chrome(options=chromeOptions)

# 파싱할 페이지로 이동
driver.get("https://www.rocketpunch.com/jobs?job=sw-developer")
WebDriverWait(driver, 10).until(expected_conditions.presence_of_all_elements_located(By.ID, "fb-root"))

# driver.get("https://www.rocketpunch.com/jobs")

# BeautifulSoup으로 html 파싱
companies = []; companies
for item in BeautifulSoup(driver.page_source, 'html.parser').find_all(attrs={"class" : "company item"}):

    #회사명/업종명
    company = {}; company
    companyName = item.find(attrs={"class":"header name"}) \
                .find(lambda x : 
                        not isinstance(x, element.NavigableString) 
                        and x.name == 'strong').text; companyName # 회사명
    company['companyNm'] = companyName; company

    info = {}
    companySectors = item.find(attrs={"class": "nowrap meta"}).get_text().strip(); companySectors # 업종명
    # company[companyName]['company-sector'] = companySectors
    info['company-sector'] = companySectors; info

    company[companyName] = info; company

    jobs = [] 
    for desc in item.find(attrs={"class": "company-jobs-detail"}).descendants:
        job = {}
        if not isinstance(desc, element.NavigableString) and 'job-detail' in desc.get_attribute_list('class'):
            job['job-title'] = desc.find(attrs={"class": "job-title"}).text; job
            job['job-stat-info'] = desc.find(attrs={"class": "job-stat-info"}).text; job
        job and jobs.append(job); jobs

    info['jobs'] = jobs; info
    company['name'] = companyName
    company['info'] = info; company
    companies.append(company); # pprint(companies)

    # 수집된 게시물을 담을 자료구조
    # 페이징 처리된 태그와 속성값을 확인 후 다음 번에 이동할 페이지를 저장하기

pprint(companies)