import logging

import pytest
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
class CheckBox(BaseDriver):
    log = Utils.custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SINGLE_CHECKBOX = "//input[@id='checkBox1']"
    CHECKBOX_3 = "//input[@id='checkBox3']"
    PRE_CHECK_CHECKBOX = "//input[@id='checkBox5']"

    def find_single_check_box(self):
        return self.driver.find_element(By.XPATH, self.SINGLE_CHECKBOX)

    def find_pre_checked_checkbox(self):
        return self.driver.find_element(By.XPATH, self.PRE_CHECK_CHECKBOX)

    def find_checkbox_group(self):
        return self.driver.find_element(By.XPATH, self.CHECKBOX_3)

    def click_single_check_box(self):
        self.find_single_check_box().click()

    def click_prechecked_checkbox(self):
        status = self.find_pre_checked_checkbox().is_selected()
        self.log.info(f"Status of pre checked checkbox: {status}")
        self.find_pre_checked_checkbox().click()

    def click_checkbox_group(self):
        self.find_checkbox_group().click()

    def click_checkbox(self):
        self.click_single_check_box()
        self.click_prechecked_checkbox()
        self.click_checkbox_group()
