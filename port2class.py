# class RocketCrawl():
#     EMPTY = None
#     def __enter__(self):
#         self.driver = webdriver.Chrome(options = self.chromeOptions)

#     def __exit__(self):
#         self.driver.quit()

#     def __init__(self, url):
#         self.chromeOptions = Options().add_argument("headless")
#         self.url = url
#         self.search = None
    
#     def getpage(self):
#         self.driver.get(self.url)
#         self.search = BeautifulSoup(driver.page_source, 'html.parser')