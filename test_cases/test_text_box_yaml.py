import time
import pytest
import softest
from pages.input_text_fields import TextFields
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class TestInputTextFields(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tf = TextFields(self.driver)

    @file_data("../test_data/text_data.yaml")
    def test_set_data_in_field(self, blank_text, text_area, prefilled_text, placeholder_text):
        self.tf.fill_data(blank_text, text_area, prefilled_text, placeholder_text)
        time.sleep(5)
