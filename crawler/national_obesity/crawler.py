import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .constants.constants import START_URL, DATASET, DATASET_XPATH


def search_element(driver, xpath):
   return  WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    
def national_crawler():
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    download_path = os.path.join(project_dir, "csv")

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_experimental_option("prefs", {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)
    driver.get(START_URL)

    wait_search = search_element(driver, DATASET_XPATH["search"])
    wait_search.send_keys(DATASET)
    wait_search.send_keys(Keys.ENTER)

    wait_link = search_element(driver, DATASET_XPATH["link"])
    wait_link.click()

    time.sleep(2)
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    wait_download = search_element(driver, DATASET_XPATH["download"])
    driver.execute_script("arguments[0].scrollIntoView()", wait_download)
    time.sleep(2)
    wait_download.click()
    time.sleep(5)

    driver.quit()