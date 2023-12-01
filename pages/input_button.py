from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class Button(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    INPUT_BUTTON = "//*[@id='myButton']"
    READ_ONLY_TEXT = "//input[@id='readOnlyText']"
    PARAGRAPH_WITH_TEXT = "//p[@id='pText']"
    # READ_ONLY_TEXT = "The Color is Purple"
    # PARAGRAPH_TEXT = "This Text is Purple"

    def get_input_button(self):
        return self.driver.find_element(By.XPATH, self.INPUT_BUTTON)

    def get_read_only_text(self):
        return self.driver.find_element(By.XPATH, self.READ_ONLY_TEXT)

    def get_paragraph_text(self):
        return self.driver.find_element(By.XPATH, self.PARAGRAPH_WITH_TEXT)

    def set_input_button(self):
        self.get_input_button().click()

    def set_read_only_text(self):
        text_value = self.get_read_only_text()
        print(f"Read only text: {text_value.get_attribute('value')}")

    def set_paragraph_text(self):
        para_value = self.get_paragraph_text().text
        print(f"Paragraph text: {para_value}")

    def check_texts(self):
        self.set_input_button()
        self.set_read_only_text()
        self.set_paragraph_text()
