import unittest

from config import browser
from locators.overlapped_element_locators import OVERLAPPED_URL, ID_INPUT, NAME_INPUT, SCROLLED_AREA


class OverlappedElementPage(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.get(OVERLAPPED_URL)

    def test_overlapped_element(self):
        id_input = self.driver.find_element(*ID_INPUT)
        id_input.send_keys("mico")
        name_input = self.driver.find_element(*NAME_INPUT)

        self.driver.execute_script(f"return document.querySelector('{SCROLLED_AREA}').scrollTo(0, 50)")

        name_input.send_keys("mucahit")

        self.assertEqual("mucahit", name_input.get_attribute("value"))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
