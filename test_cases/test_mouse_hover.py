import pytest
import softest
from pages.mouse_hover import MouseHover


@pytest.mark.usefixtures("setup")
class TestMouseHover(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.mh = MouseHover(self.driver)

    def test_hover(self):
        self.mh.click_menu_options()
