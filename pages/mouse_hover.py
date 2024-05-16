import logging
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class MouseHover(BaseDriver):
    log = Utils.custom_logger(log_level=logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    HOVER_DROPDOWN = "//div[@id='myDropdown']"
    HOVER_LINK_ONE = "//a[@id='dropOption1']"
    HOVER_LINK_TWO = "//a[@id='dropOption2']"
    HOVER_LINK_THREE = "//a[@id='dropOption3']"
    OPTION_ONE_TEXT = "//h3[contains(text(),'Link One Selected')]"
    OPTION_TWO_TEXT = "//h3[contains(text(),'Link Two Selected')]"
    OPTION_THREE_TEXT = "//h3[contains(text(),'Link Three Selected')]"

    def get_hover_dropdown(self):
        hover_dd = self.driver.find_element(By.XPATH, self.HOVER_DROPDOWN)
        actions = ActionChains(self.driver)
        return actions.move_to_element(hover_dd).perform()

    def get_hover_dropdown_one(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.HOVER_LINK_ONE)
        return actions.move_to_element(element).click().perform()

    def get_hover_dropdown_two(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.HOVER_LINK_TWO)
        return actions.move_to_element(element).click().perform()

    def get_hover_dropdown_three(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, self.HOVER_LINK_THREE)
        return actions.move_to_element(element).click().perform()

    def click_hover_option_one(self):
        self.get_hover_dropdown()
        self.get_hover_dropdown_one()
        text_value = self.driver.find_element(By.XPATH, self.OPTION_ONE_TEXT)
        self.log.info(f"You clicked: {text_value.get_attribute('innerHTML')}")
        time.sleep(1)

    def click_hover_option_two(self):
        self.get_hover_dropdown()
        self.get_hover_dropdown_two()
        text_value = self.driver.find_element(By.XPATH, self.OPTION_TWO_TEXT)
        self.log.info(f"You clicked: {text_value.get_attribute('innerHTML')}")
        time.sleep(2)

    def click_hover_option_three(self):
        self.get_hover_dropdown()
        self.get_hover_dropdown_three()
        text_value = self.driver.find_element(By.XPATH, self.OPTION_THREE_TEXT)
        self.log.info(f"You clicked: {text_value.get_attribute('innerHTML')}")
        time.sleep(3)

    def click_menu_options(self):
        self.click_hover_option_one()
        self.click_hover_option_two()
        self.click_hover_option_three()
