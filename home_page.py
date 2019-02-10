from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage(BasePage):
    base_url = 'https://www.gmail.com'

    def login(self, email, password):
        self.driver.get(self.base_url)

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.ID, "identifierId")))
        self.driver.find_element_by_id('identifierId').send_keys(email)
        self.click(id='identifierNext')

        self.driver.find_element_by_name('password').send_keys(password)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Далее')]")))

        self.click(xpath="//span[contains(text(),'Далее')]")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class ='T-I J-J5-Ji T-I-KE L3']")))

    def send_mail(self, mail_name2, text_mail):
        self.driver.find_element_by_xpath("//div[@class ='T-I J-J5-Ji T-I-KE L3']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//div[@class ='wO nr l1'] // textarea[@ name='to']")))

        self.driver.find_element_by_xpath("//div[@class ='wO nr l1'] // textarea[@ name='to']").send_keys(mail_name2)
        self.driver.find_element_by_xpath("//input[@placeholder = 'Тема']").send_keys('Test')
        self.driver.find_element_by_xpath("//div[@class ='Am Al editable LW-avf']").send_keys(text_mail)
        self.driver.find_element_by_xpath("//div[@class ='T-I J-J5-Ji aoO T-I-atl L3']").click()

    def move_to_sending_email(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
            (By.XPATH, "//a[@title = 'Отправленные']")))

        self.driver.find_element_by_xpath("//a[@title = 'Отправленные']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//div[@class='BltHke nH oy8Mbf']//div//tbody//tr[1]")))

        self.driver.find_element_by_xpath("//div[@class='BltHke nH oy8Mbf']//div//tbody//tr[1]").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.NAME, 'epamtestemail2')))

    def logout(self):
        self.click(xpath="//span[@class='gb_cb gbii']")
        self.click(xpath="//a[@class='gb_Aa gb_Ag gb_Ig gb_ff gb_Tb']")

    def click_to_incoming_message(self):
        self.driver.find_element_by_xpath("//div[@class='aDP']//div//div//div//tbody/tr[1]").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.NAME, 'epamtestemail2')))


#     def setEmail(self, email):
#         self.fill_form_by_id("id_email", email)
#
#     def setPassword(self, password):
#         self.fill_form_by_id("id_password", password)
#
#     def submit(self):
#         self.driver.find('#create_account_form button').click()
