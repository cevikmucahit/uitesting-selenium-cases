import unittest

from config import browser
from locators.text_input_locators import TEXT_INPUT_URL, BUTTON, INPUT


class TextinputPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(TEXT_INPUT_URL)

    def test_text_input(self):
        text_input = self.driver.find_element(*INPUT)
        text_input.send_keys("Germiyan Oguzhan")

        button = self.driver.find_element(*BUTTON)
        button.click()

        self.assertEqual("Germiyan Oguzhan", button.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
