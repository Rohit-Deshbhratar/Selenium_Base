from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class RadioButton(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    RADIO_BUTTON_2 = "//input[@id='radioButton2']"

    def get_radio_button(self):
        return self.driver.find_element(By.XPATH, self.RADIO_BUTTON_2)

    def click_radio_button(self):
        self.get_radio_button().click()
