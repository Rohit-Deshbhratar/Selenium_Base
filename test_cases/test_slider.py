import time

import pytest
import softest
from pages.sliders import Sliders


@pytest.mark.usefixtures("setup")
class TestSliders(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.slider = Sliders(self.driver)

    def test_slider(self):
        self.slider.set_slider_to_right()
        self.slider.set_slider_to_left()
        time.sleep(4)
