import time
import pytest
import softest
from pages.input_text_fields import TextFields
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestInputTextFields(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tf = TextFields(self.driver)

    @data(("Rohit", "This is text area.", "This is new text.", "Hello"))
    @unpack
    def test_set_data_in_field(self, blank_text, text_area, prefilled_text, placeholder_text):
        self.tf.fill_data(blank_text, text_area, prefilled_text, placeholder_text)
        time.sleep(5)
