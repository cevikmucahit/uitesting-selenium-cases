import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.ajax_locators import AJAX_URL, BUTTON, RESPONSE


class AjaxPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(AJAX_URL)

    def test_load_data(self):
        button = self.driver.find_element(*BUTTON)
        button.click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.text_to_be_present_in_element(RESPONSE, "Data loaded with AJAX get request."))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
