from selenium import webdriver
from bs4 import BeautifulSoup
from bs4 import element
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pprint import pprint
import time

def main():
    chromeOptions = Options()
    chromeOptions.add_argument('headless')
    driver = webdriver.Chrome('/Users/yoonsung0711/git/getjobcrawl/chromedriver', options=chromeOptions)

    driver.get('https://www.rocketpunch.com/jobs?job=sw-developer')
    # WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'fb-root')))
    time.sleep(1)

    companies = []
    for item in BeautifulSoup(driver.page_source, 'html.parser').find_all(attrs={'class': 'company item'}):
        time.sleep(1)
        company = {}
        companyName = item.find(attrs={'class': 'header name'}) \
                    .find(lambda x : 
                        not isinstance(x, element.NavigableString)
                        and x.name == 'strong').text
        company['companyNm'] = companyName

        info = {}
        companySectors = item.find(attrs={'class': 'nowrap meta'}).get_text().strip()
        info['company-sector'] = companySectors

        company[companyName] = info

        jobs = []
        for desc in item.find(attrs={'class': 'company-jobs-detail'}).descendants:
            job = {}
            if not isinstance(desc, element.NavigableString) and 'job-detail' in desc.get_attribute_list('class'):
                job['job-title'] = desc.find(attrs={'class': 'job-title'}).text
                job['job-stat-info'] = desc.find(attrs={'class': 'job-stat-info'}).text
            job and jobs.append(job)

        info['jobs'] = jobs
        company['name'] = companyName
        company['info'] = info
        companies.append(company)
        driver.quit()

    pprint(companies)

if __name__ == '__main__':
    main()