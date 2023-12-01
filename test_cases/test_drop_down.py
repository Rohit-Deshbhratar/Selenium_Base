import pytest
import softest
from pages.select_drop_down import SelectDropDown


@pytest.mark.usefixtures("setup")
class TestDropDown(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.dd = SelectDropDown(self.driver)

    def test_click_dropdown(self):
        self.dd.select_dropdown()
