import unittest

from config import browser
from locators.button_alert_locators import BUTTON, BUTTON_ALERT_URL


class ButtonAlertPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = browser()
        cls.driver.get(BUTTON_ALERT_URL)

    def test_button_alert(self):
        button = self.driver.find_element(*BUTTON)
        button.click()

        alert = self.driver.switch_to.alert
        alert.accept()

        self.assertEqual(self.driver.switch_to.active_element, button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
