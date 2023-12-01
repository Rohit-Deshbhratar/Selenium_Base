from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class Iframes(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    IFRAME_FOR_CHECKBOX = "//iframe[@id='myFrame3']"
    CHECKBOX_INSIDE_IFRAME = "//*[@id='checkBox6']"
    IFRAME_TEXT = "//iframe[@id='myFrame2']"
    TEXT_INSIDE_IFRAME = "/html/body/h4"

    def get_text_inside_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.IFRAME_TEXT))
        return self.driver.find_element(By.XPATH, self.TEXT_INSIDE_IFRAME)

    def get_checkbox_inside_iframe(self):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.IFRAME_FOR_CHECKBOX))
        return self.driver.find_element(By.XPATH, self.CHECKBOX_INSIDE_IFRAME)

    def get_out_of_iframe(self):
        return self.driver.switch_to.default_content()

    def set_text_inside_iframe(self):
        value = self.get_text_inside_iframe()
        print(f"Text inside iframe: {value.get_attribute('innerHTML')}")

    def set_inside_iframe(self):
        self.get_checkbox_inside_iframe().click()

    def in_iframe(self):
        self.set_inside_iframe()
        self.get_out_of_iframe()
        self.set_text_inside_iframe()
