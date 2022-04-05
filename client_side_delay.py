import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.client_delay_locators import CLIENT_URL, DATA, BUTTON


class ClientPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(CLIENT_URL)

    def test_client_delay(self):
        button = self.driver.find_element(*BUTTON)
        button.click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.text_to_be_present_in_element(DATA, "Data calculated on the client side."))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
