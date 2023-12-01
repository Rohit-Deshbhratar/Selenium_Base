import time
import pytest
import softest
from pages.input_radio_button import RadioButton


@pytest.mark.usefixtures("setup")
class TestRadioButton(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.rb = RadioButton(self.driver)

    def test_click_radio_button(self):
        self.rb.click_radio_button()
        time.sleep(3)
