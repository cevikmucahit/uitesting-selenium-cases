import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.verifiy_locators import VERIFY_TEXT_URL, TEXT


class VerifyTextPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(VERIFY_TEXT_URL)

    def test_get_text(self):
        wait = WebDriverWait(self.driver, 30)

        wait.until(ec.text_to_be_present_in_element(TEXT, "Welcome"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
