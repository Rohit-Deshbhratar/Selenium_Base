import time
import pytest
import softest
from pages.input_checkbox import CheckBox


@pytest.mark.usefixtures("setup")
class TestCheckbox(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.cb = CheckBox(self.driver)

    def test_click_checkbox(self):
        self.cb.click_checkbox()
        time.sleep(5)
