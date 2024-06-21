import time
import logging
from selenium.webdriver.common.by import By
from demoframework.utilities.utils import Utils
from selenium.webdriver.common.keys import Keys
from demoframework.base.base_driver import BaseDriver
from demoframework.pages.search_flights_results_page import SearchFlightResults


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    depart_from_field = "//input[@id='BE_flight_origin_city']"
    going_to_field = "//input[@id='BE_flight_arrival_city']"
    select_date_field = "//input[@id='BE_flight_origin_date']"
    all_date = "//div[@id='monthWrapper']//tbody/tr/td"
    search_btn_field = "//input[@value='Search Flights']"
    all_going_to_result = "//div[@class='ac_results dest_ac']//div/li//p[1]"

    def retrieved_get_depart_from_field(self):
        return self.wait_for_element_clickable(By.XPATH, self.depart_from_field)

    def retrieved_get_going_to_field(self):
        time.sleep(2)
        return self.wait_for_element_clickable(By.XPATH, self.going_to_field)

    def retrieved_select_date_field(self):
        return self.wait_for_element_clickable(By.XPATH, self.select_date_field)

    def retrieved_btn_search(self):
        time.sleep(1)
        return self.wait_for_element_clickable(By.XPATH, self.search_btn_field)

    def enter_depart_from_location(self,depart_location):
        self.retrieved_get_depart_from_field().click()
        self.log.info("clicked on going to")
        self.retrieved_get_depart_from_field().send_keys(depart_location)
        self.log.info("Typed text into going to field successfully")
        self.retrieved_get_depart_from_field().send_keys(Keys.ENTER)

    def enter_going_to_location(self,going_to_location):
        self.retrieved_get_going_to_field().send_keys(going_to_location)
        time.sleep(2)
        all_going_to_results = self.wait_for_presence_of_all_elements(By.XPATH, self.all_going_to_result)
        for results in all_going_to_results:
            if "Mumbai (BOM)" in results.text:
                time.sleep(2)
                results.click()
                break

    def enter_selected_date(self,departure_date):
        time.sleep(1)
        self.retrieved_select_date_field().click()
        all_dates = self.wait_for_presence_of_all_elements(By.XPATH, self.all_date)
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                date.click()
                break

    def click_btn_search(self):
        self.driver.execute_script("arguments[0].click();", self.retrieved_btn_search())

    def search_flights(self, depart_location, going_to_location, departure_date):
        self.enter_depart_from_location(depart_location)
        self.enter_going_to_location(going_to_location)
        self.enter_selected_date(departure_date)
        self.click_btn_search()
        search_flights_results = SearchFlightResults(self.driver)
        return search_flights_results

