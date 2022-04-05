import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from config import browser
from locators.sample_app_locators import SAMPLE_APP_URL, USER_NAME_INPUT, PASSWORD_INPUT, LOGIN_BUTTON, EXPECTED_ELEMENT


class SampleAppPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(SAMPLE_APP_URL)

    def test_sample_app(self):
        username_input = self.driver.find_element(*USER_NAME_INPUT)
        username_input.send_keys("micocevik")

        password_input = self.driver.find_element(*PASSWORD_INPUT)
        password_input.send_keys("pwd")

        login_button = self.driver.find_element(*LOGIN_BUTTON)
        login_button.click()

        wait = WebDriverWait(self.driver, 30)
        wait.until(ec.presence_of_element_located(EXPECTED_ELEMENT))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
