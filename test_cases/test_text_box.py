import time
import pytest
import softest
from pages.input_text_fields import TextFields


@pytest.mark.usefixtures("setup")
class TestInputTextFields(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tf = TextFields(self.driver)

    def test_set_data_in_field(self):
        self.tf.fill_data("Rohit", "This is text area.", "This is new text.", "Hello")
        time.sleep(5)
