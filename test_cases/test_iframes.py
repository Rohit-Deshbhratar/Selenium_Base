import time

import pytest
import softest
from pages.iframes import Iframes


@pytest.mark.usefixtures("setup")
class TestIframes(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.iframes = Iframes(self.driver)

    def test_inside_iframes(self):
        self.iframes.in_iframe()
        time.sleep(4)
