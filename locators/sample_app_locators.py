from selenium.webdriver.common.by import By

SAMPLE_APP_URL = "http://uitestingplayground.com/sampleapp"
USER_NAME_INPUT = (By.NAME, "UserName")
PASSWORD_INPUT = (By.NAME, "Password")
EXPECTED_ELEMENT = (By.CLASS_NAME, "text-success")
LOGIN_BUTTON =(By.ID, "login")