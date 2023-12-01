import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver


class Sliders(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    SLIDER = "//input[@id='mySlider']"

    def get_slider(self):
        return self.driver.find_element(By.XPATH, self.SLIDER)

    def set_slider_to_right(self):
        time.sleep(3)
        ActionChains(self.driver).drag_and_drop_by_offset(self.get_slider(), 30, 0).perform()

    def set_slider_to_left(self):
        time.sleep(3)
        ActionChains(self.driver).drag_and_drop_by_offset(self.get_slider(), -50, 0).perform()
