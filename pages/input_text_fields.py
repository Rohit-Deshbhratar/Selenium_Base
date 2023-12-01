from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class TextFields(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    BLANK_TEXT_FIELD = "//input[@id='myTextInput']"
    BLANK_TEXT_AREA = "//textarea[@id='myTextarea']"
    PREFILLED_TEXT_FIELD = "//input[@id='myTextInput2']"
    PLACEHOLDER_TEXT_FIELD = "//input[@id='placeholderText']"

    def get_blank_text_field(self):
        return self.driver.find_element(By.XPATH, self.BLANK_TEXT_FIELD)

    def get_blank_text_area(self):
        return self.driver.find_element(By.XPATH, self.BLANK_TEXT_AREA)

    def get_prefilled_text_field(self):
        return self.driver.find_element(By.XPATH, self.PREFILLED_TEXT_FIELD)

    def get_placeholder_text_field(self):
        return self.driver.find_element(By.XPATH, self.PLACEHOLDER_TEXT_FIELD)

    def set_text_in_blank_text_field(self, data):
        self.get_blank_text_field().click()
        self.get_blank_text_field().send_keys(data)

    def set_text_in_text_area(self, data):
        self.get_blank_text_area().click()
        self.get_blank_text_area().send_keys(data)

    def set_text_in_prefilled_text_field(self, data):
        value = self.get_prefilled_text_field()
        print(f"Before entering text: {value.get_attribute('value')}")
        self.get_prefilled_text_field().click()
        self.get_prefilled_text_field().clear()
        self.get_prefilled_text_field().send_keys(data)

    def set_placeholder_text_field(self, data):
        self.get_placeholder_text_field().click()
        self.get_placeholder_text_field().send_keys(data)

    def fill_data(self, blank_text, text_area, prefilled_text, placeholder_text):
        self.set_text_in_blank_text_field(blank_text)
        self.set_text_in_text_area(text_area)
        self.set_text_in_prefilled_text_field(prefilled_text)
        self.set_placeholder_text_field(placeholder_text)
