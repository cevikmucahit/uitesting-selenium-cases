import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.progress_bar_locators import PROGRESS_BAR_URL, STOP_BUTTON, START_BUTTON, BAR


class ProgressbarPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(PROGRESS_BAR_URL)

    def test_progress_bar(self):
        start_button = self.driver.find_element(*START_BUTTON)
        stop_button = self.driver.find_element(*STOP_BUTTON)
        bar = self.driver.find_element(*BAR)

        start_button.click()

        while True:
            if int(bar.get_attribute("aria-valuenow")) >= 75:
                stop_button.click()
                break

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
