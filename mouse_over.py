import unittest

from selenium.webdriver.common.action_chains import ActionChains

from config import browser
from locators.mouse_over_locators import MOUSE_OVER_URL, CLICK_LINK, CLICK_COUNT


class MouseoverPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(MOUSE_OVER_URL)

    def test_mouse_over(self):
        click_link = self.driver.find_element(*CLICK_LINK)
        click_count = self.driver.find_element(*CLICK_COUNT)

        action = ActionChains(self.driver)
        action.double_click(click_link).perform()

        self.assertEqual("2", click_count.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
