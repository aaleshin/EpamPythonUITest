from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, xpath=None, id=None):
        if id is not None:
            self.driver.find_element_by_id(id).click()
        elif xpath is not None:
            self.driver.find_element_by_xpath(xpath).click()

    def wait_element_to_be_clickable(self, xpath=None, id=None, name=None):
        if id is not None:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, id)))
        elif xpath is not None:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))
        elif name is not None:
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, name)))

    def send_key(self, text, xpath=None, id=None, name=None):
        if id is not None:
            self.driver.find_element_by_id(id).send_keys(text)
        elif xpath is not None:
            self.driver.find_element_by_xpath(xpath).send_keys(text)
        elif name is not None:
            self.driver.find_element_by_name(name).send_keys(text)

    def get_web_element(self, xpath=None, name=None):
        if xpath is not None:
            return self.driver.find_element_by_xpath(xpath)
        elif name is not None:
            return self.driver.find_element_by_name(name)
