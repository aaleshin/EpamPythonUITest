from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):
    MAILINPUT = 'identifierId'
    NEXTBUTTON = 'identifierNext'
    PASSWORDINPUT = 'password'
    FINISHLOGIN = "//span[contains(text(),'Далее')]"

    def login(self, email, password):
        self.wait_element_to_be_clickable(id=self.MAILINPUT)
        self.send_key(email, id=self.MAILINPUT)
        self.click(id=self.NEXTBUTTON)
        self.send_key(password, name=self.PASSWORDINPUT)
        self.wait_element_to_be_clickable(xpath=self.FINISHLOGIN)
        self.click(xpath=self.FINISHLOGIN)

        return HomePage(self.driver)


class HomePage(BasePage):
    NEWMAILBUTTON = "//div[@class ='T-I J-J5-Ji T-I-KE L3']"
    NAMETOINPUT = "//div[@class ='wO nr l1'] // textarea[@ name='to']"
    THEMENAME = "//input[@placeholder = 'Тема']"
    TEXTMAILINPUT = "//div[@class ='Am Al editable LW-avf']"
    SENDEMAILBUTTON = "//div[@class ='T-I J-J5-Ji aoO T-I-atl L3']"

    def send_mail(self, mail_name2, text_mail, test_text):
        self.wait_element_to_be_clickable(xpath=self.NEWMAILBUTTON)
        self.click(xpath=self.NEWMAILBUTTON)

        self.wait_element_to_be_clickable(xpath=self.NAMETOINPUT)
        self.send_key(mail_name2, xpath=self.NAMETOINPUT)
        self.send_key(test_text, xpath=self.THEMENAME)
        self.send_key(text_mail, xpath=self.TEXTMAILINPUT)

        self.wait_element_to_be_clickable(xpath=self.SENDEMAILBUTTON)
        self.click(xpath=self.SENDEMAILBUTTON)

        return SendingPage(self.driver)


class SendingPage(HomePage):
    SENDINGLINK = "//a[@title = 'Отправленные']"
    FIRSTMAILLINK = "//div[@class='BltHke nH oy8Mbf']//div//tbody//tr[1]"
    OPENMAIL = 'epamtestemail2'
    MAILNAME = "//h2[@class='hP']"
    MAILTEXT = "//div[contains(text(),'chrome')]"

    def move_to_sending_email(self):
        self.wait_element_to_be_clickable(xpath=self.SENDINGLINK)
        self.click(xpath=self.SENDINGLINK)

        self.wait_element_to_be_clickable(xpath=self.FIRSTMAILLINK)
        self.click(xpath=self.FIRSTMAILLINK)

        self.wait_element_to_be_clickable(name=self.OPENMAIL)

    def get_sending_data(self):
        send_to_name = self.get_web_element(name=self.OPENMAIL)
        return send_to_name.text

    def get_mail_name(self):
        mail_name = self.get_web_element(xpath=self.MAILNAME)
        return mail_name.text

    def get_mail_text(self):
        mail_text = self.get_web_element(xpath=self.MAILTEXT)
        return mail_text.text

    # def logout(self):
    #     self.click(xpath="//span[@class='gb_cb gbii']")
    #     self.click(xpath="//a[@class='gb_Aa gb_Ag gb_Ig gb_ff gb_Tb']")
    #
    # def click_to_incoming_message(self):
    #     self.driver.find_element_by_xpath("//div[@class='aDP']//div//div//div//tbody/tr[1]").click()
    #     WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
    #         (By.NAME, 'epamtestemail2')))
