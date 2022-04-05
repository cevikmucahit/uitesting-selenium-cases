from selenium.webdriver.common.by import By

VISIBILITY_URL = "http://uitestingplayground.com/visibility"
HIDE_BUTTON = (By.ID, "hideButton")
ALL_BUTTON = (By.CSS_SELECTOR, "table button:not(#hideButton)")


