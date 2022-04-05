import unittest

from selenium.common.exceptions import ElementClickInterceptedException

from config import browser
from locators.z_index_locators import Z_URL, GREEN_BUTTON, BLUE_BUTTON


class ZPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(Z_URL)

    def test_button_is_clickable(self):
        try:
            green_button = self.driver.find_element(*GREEN_BUTTON)
            green_button.click()
            green_button.click()

            self.assertTrue(False)
        except ElementClickInterceptedException:
            pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
