import os, requests
from bs4 import BeautifulSoup
import spotipy

req = requests.get("http://ben-tanen.com")

if req.status_code == 200:
    soup = BeautifulSoup(req.text, "html.parser")
    print(soup.prettify()[:200])

### TESTING WITH SELENIUM INSTANCE

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# setting up headless driver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)

driver.get("http://ben-tanen.com/")

cells = driver.find_elements_by_xpath("//div[contains(@class, 'proj-cell')]")
print([cell.get_attribute("innerText") for cell in cells])

cells[0].click()
print(driver.current_url)

driver.quit()