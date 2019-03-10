import pytest
from selenium import webdriver
import selenium
from datetime import datetime
from home_page import LoginPage
from hamcrest import assert_that, contains_string, equal_to

# import allure

base_url = 'https://www.gmail.com'
mail_name1 = 'epamtestemail1@gmail.com'
pass1 = 'Ac1234567890'
mail_name2 = 'epamtestemail2@gmail.com'
pass2 = 'Ac1234567890xA'
date = datetime.strftime(datetime.now(), "%Y.%m.%d")
test_text = 'TEST'


class Test2GoogleLetters:
    @pytest.yield_fixture(scope='session')
    def driver(self):
        # Before starting the test, copy chromedriver from http: // www.seleniumhq.org / download / and enter correct PATH.!!
        driver = selenium.webdriver.Chrome("D:\\downloads\\avtotests\\chromedriver.exe")
        driver.get(base_url)
        driver.implicitly_wait(30)
        driver.fullscreen_window()
        yield driver
        driver.quit()

    def test_send_letters(self, driver):
        browser_name = driver.name
        text_mail = date + ' ' + browser_name

        loginpage = LoginPage(driver)
        homepage = loginpage.login(mail_name1, pass1)
        sendingpage = homepage.send_mail(mail_name2, text_mail, test_text)
        sendingpage.move_to_sending_email()

        assert_that(sendingpage.get_sending_data(), contains_string('epamtestemail2'))
        assert_that(sendingpage.get_mail_name(), equal_to(test_text))
        assert_that(sendingpage.get_mail_text(), equal_to(text_mail))

        # homepage.logout()
        # homepage.login(mail_name2, pass2)
        # homepage.click_to_incoming_message()

        # send_from_name = driver.find_element_by_name('epamtestemail2').text
        # assert_that(mail_name, equal_to("Test"))
        # assert_that(send_from_name, contains_string('epamtestemail2'))
        # assert_that(mail_text, equal_to(text_mail))
