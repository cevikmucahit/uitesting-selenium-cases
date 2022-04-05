import unittest

from selenium.webdriver.common.action_chains import ActionChains

from config import browser
from locators.scrollbars_locators import SCROLLBARS_URL, BUTTON


class ScrollbarsPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(SCROLLBARS_URL)

    def test_scroll_bars(self):
        button = self.driver.find_element(*BUTTON)

        action = ActionChains(self.driver)
        action.move_to_element(button).click().perform()

        self.assertEqual(self.driver.switch_to.active_element, button)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
