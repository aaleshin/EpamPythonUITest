class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, xpath=None, id=None, name=None):
        if name is not None:
            self.driver.find_element_by_name(name).click()
        elif id is not None:
            self.driver.find_element_by_id(id).click()
        elif xpath is not None:
            self.driver.find_element_by_xpath(xpath).click()





#     def fill_form_by_css(self, form_css, value):
#         elem = self.driver.find(form_css)
#         elem.send_keys(value)
#
#     def fill_form_by_id(self, form_element_id, value):
#         return self.fill_form_by_css('#%s' % form_element_id, value)
#
#     def navigate(self):
#         self.driver.get(self.url)
