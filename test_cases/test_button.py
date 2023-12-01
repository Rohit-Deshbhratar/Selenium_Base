import time

import pytest
import softest
from pages.input_button import Button


@pytest.mark.usefixtures("setup")
class TestButton(softest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.tb = Button(self.driver)

    def test_after_click(self):
        self.tb.check_texts()
        time.sleep(4)
