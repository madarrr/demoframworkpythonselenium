import logging
import time
import logging
from selenium.webdriver.common.by import By
from demoframework.utilities.utils import Utils
from demoframework.base.base_driver import BaseDriver


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(loglevel=logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    filter_1_stop_btn_field = "//*[@id='Flight-APP']/section/section[1]/div/div[1]/div/div[2]/div[2]/label[2]/p"
    filter_2_stop_btn_field = "//*[@id='Flight-APP']/section/section[1]/div/div[1]/div/div[2]/div[2]/label[3]/p"
    filter_0_stop_btn_field = "//*[@id='Flight-APP']/section/section[1]/div/div[1]/div/div[2]/div[2]/label[1]/p"
    all_stop_field = "//span[contains(text(), 'non stop') or contains(text(), '1 Stop')]"

    def retrieved_filter_1_stop_btn(self):
        return self.driver.find_element(By.XPATH, self.filter_1_stop_btn_field)

    def retrieved_filter_2_stop_btn(self):
        return self.driver.find_element(By.XPATH, self.filter_2_stop_btn_field)

    def retrieved_filter_0_stop_btn(self):
        return self.driver.find_element(By.XPATH, self.filter_0_stop_btn_field)

    def get_search_flights_result(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.all_stop_field)

    def click_on_filter_btn(self, by_stop):
        if by_stop == "1 Stop":
            self.retrieved_filter_1_stop_btn().click()
            self.log.warning("Selected flights with 1 Stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.retrieved_filter_2_stop_btn().click()
            self.log.warning("Selected flights with 2 Stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.retrieved_filter_0_stop_btn().click()
            self.log.warning("Selected flights with Non Stop")
            time.sleep(2)
        else:
            self.log.warning("Please Provide valid filter options")