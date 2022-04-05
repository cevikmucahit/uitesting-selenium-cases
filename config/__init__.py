from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(log_level=0).install()))
    driver.maximize_window()
    return driver


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC