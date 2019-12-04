from selenium import webdriver

from bs4 import BeautifulSoup as BS
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chromeOptions = Options()
# chromeOptions.add_argument("--kiosk")
chromeOptions.add_argument("headless")
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.rocketpunch.com/jobs?job=sw-developer")

job_ads  = driver.find_elements_by_class_name("job-detail")
dir(job_ads)

job_ads_bs = BS(job_ads)

for ad in job_ads: 
    title = ad.find_element_by_class_name("job-title").text
    info = ad.find_element_by_class_name("job-stat-info").text
    end = ad.find_element(By.CSS_SELECTOR, ".job-dates>span").text
    print("직무:" + title, "\n구분:" + info, "\n마감일:" + end + "\n")


# type(jobs)
# for j in jobs:
#     print(j.text)
# jobinfo = body.find_elements_by_class_name("job-stat-info")
# type(jobinfo)
# for info in jobinfo:
#     print(info.text)


# dir(body)
driver.quit()


 