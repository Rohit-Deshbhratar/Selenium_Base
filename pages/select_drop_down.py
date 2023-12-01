import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class SelectDropDown(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    DROPDOWN_OPTION_ONE = "//*[@id='mySelect']/option[1]"
    DROPDOWN_OPTION_TWO = "//*[@id='mySelect']/option[2]"
    DROPDOWN_OPTION_THREE = "//*[@id='mySelect']/option[3]"
    DROPDOWN_OPTION_FOUR = "//*[@id='mySelect']/option[4]"

    def get_dropdown_option_one(self):
        return self.driver.find_element(By.XPATH, self.DROPDOWN_OPTION_ONE)

    def get_dropdown_option_two(self):
        return self.driver.find_element(By.XPATH, self.DROPDOWN_OPTION_TWO)

    def get_dropdown_option_three(self):
        return self.driver.find_element(By.XPATH, self.DROPDOWN_OPTION_THREE)

    def get_dropdown_option_four(self):
        return self.driver.find_element(By.XPATH, self.DROPDOWN_OPTION_FOUR)

    def set_dropdown_option_one(self):
        self.get_dropdown_option_one().click()
        time.sleep(2)

    def set_dropdown_option_two(self):
        self.get_dropdown_option_two().click()
        time.sleep(3)

    def set_dropdown_option_three(self):
        self.get_dropdown_option_three().click()
        time.sleep(3)

    def set_dropdown_option_four(self):
        self.get_dropdown_option_four().click()
        time.sleep(2)

    def select_dropdown(self):
        self.set_dropdown_option_three()
        self.set_dropdown_option_two()
        self.set_dropdown_option_one()
        self.set_dropdown_option_four()
