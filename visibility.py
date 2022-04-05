import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.visibility_locators import VISIBILITY_URL, HIDE_BUTTON, ALL_BUTTON


class VisibilityElementPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(VISIBILITY_URL)

    def test_buttons_visibility(self):
        hide_button = self.driver.find_element(*HIDE_BUTTON)
        hide_button.click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.invisibility_of_element(ALL_BUTTON))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
