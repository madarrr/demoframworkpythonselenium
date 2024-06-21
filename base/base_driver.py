import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        page_length = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var page_length=document.body.scrollHeight;")
        match = False
        while not match:
            last_count = page_length
            time.sleep(3)
            page_length = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var page_length=document.body.scrollHeight;")
            if last_count == page_length:
                match = True
        time.sleep(4)

    def wait_for_presence_of_all_elements(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_element = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_element

    def wait_for_element_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

