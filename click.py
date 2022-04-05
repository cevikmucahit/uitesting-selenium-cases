import unittest

import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

from config import browser
from locators.click_locators import CLICK_URL, BUTTON


class ClickPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(CLICK_URL)

    def test_mouse_click(self):
        button = self.driver.find_element(*BUTTON)

        action = ActionChains(self.driver)
        action.move_to_element(button).click().perform()

        self.assertEqual(self.driver.switch_to.active_element, button)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
