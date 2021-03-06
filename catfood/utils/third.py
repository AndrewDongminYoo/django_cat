
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from catfood.models import Crawler
from first import result, Formula, Brand
import time


class WebScrapper:
    options = Options()
    options.add_argument("--window-size=1545,1047")
    options.add_argument("--window-position=0,0")

    def __init__(self, brand_name):
        self.brand_name = brand_name
        self.url_list = result[brand_name]

    def crawl(self, crawler: Crawler):
        with Chrome(options=self.options) as driver:
            driver.implicitly_wait(10)
            for index, url in enumerate(self.url_list):
                driver.get(url)
                item = Formula.objects.get_or_create(url=url)[0]
                item.brand = Brand.objects.get_or_create(en_name=self.brand_name)[0]
                item.title = driver.title
                next_value = ""
                try:
                    time.sleep(3)
                    WebDriverWait(driver, 8).until(EC.presence_of_all_elements_located((By.TAG_NAME, "p")))
                    soup = BeautifulSoup(driver.page_source, "html.parser")
                    if crawler.analysis:
                        next_value = "analysis"
                        item.analysis = soup.select_one(crawler.analysis).get_text().replace("\n", " ")
                    if crawler.ingredients:
                        next_value = "ingredients"
                        item.ingredients = soup.select_one(crawler.ingredients).get_text().replace("\n", " ")
                    if crawler.calorie:
                        next_value = "calorie"
                        item.calorie = soup.select_one(crawler.calorie).get_text()
                    item.save()
                    print(f"Saved ({index+1}/{len(self.url_list)}) :: {url}")
                except TimeoutException:
                    print(f"Timeout ({index+1}/{len(self.url_list)}) :: {url}")
                except AttributeError as e:
                    print(f"{e} :: {url}".replace("NoneType", next_value))
