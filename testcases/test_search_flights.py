import pytest
import logging
import softest
from demoframework.utilities.utils import Utils
from demoframework.pages.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()

    # Pull back class creation object
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    def test_search_flights_1_stop(self):
        # Launching browser and opening travel website
        # Code refactor
        search_flighty = self.lp.search_flights("New Delhi", "Mumbai",  "22/06/2024")
        self.lp.page_scroll()
        # Select filter 1 stop
        search_flighty.click_on_filter_btn("1 Stop")
        # Get all stop after search
        all_stop = search_flighty.get_search_flights_result()
        self.log.info(len(all_stop))
        # Assert verification
        self.ut.assert_list_item_text(all_stop, "1 Stop")

    # def test_search_flights_0_stop(self):
    #     # Launching browser and opening travel website
    #     # Code refactor
    #     search_flighty = self.lp.search_flights("New Delhi", "Mumbai",  "24/06/2024")
    #     self.lp.page_scroll()
    #     # Select filter 1 stop
    #     search_flighty.click_on_filter_btn("Non Stop")
    #     # Get all stop after search
    #     all_stop = search_flighty.get_search_flights_result()
    #     print(all_stop)
    #     # Assert verification
    #     self.ut.assert_list_item_text(all_stop,"2 Stop")
