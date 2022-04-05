import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.delay_locators import HOME_URL, DELAY_HREF, BUTTON


class DelayPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(HOME_URL)

    def test_load_delay(self):
        delay_href = self.driver.find_element(*DELAY_HREF)
        delay_href.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.presence_of_element_located(BUTTON))

        button = self.driver.find_element(*BUTTON)
        button.click()

        self.assertEqual(self.driver.switch_to.active_element, button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
