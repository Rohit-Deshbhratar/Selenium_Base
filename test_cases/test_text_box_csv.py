import time
import pytest
import softest
from pages.input_text_fields import TextFields
from ddt import ddt, data, unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
@ddt
class TestInputTextFields(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tf = TextFields(self.driver)

    @data(*Utils.read_data_from_csv("D:\\MyThings\\Development\\Selenium\\Selenium_Base\\test_data\\text_data_csv.csv"))
    @unpack
    def test_set_data_in_field(self, blank_text, text_area, prefilled_text, placeholder_text):
        self.tf.fill_data(blank_text, text_area, prefilled_text, placeholder_text)
        time.sleep(5)
