import unittest

from selenium.webdriver.common.by import By

from config import browser
from locators.dynamic_id_locators import DYNAMIC_URL, BUTTON


class DynamicPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(DYNAMIC_URL)

    def test_dynamic_id(self):
        button = self.driver.find_element(*BUTTON)
        button.click()

        self.assertEqual(self.driver.switch_to.active_element, button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
