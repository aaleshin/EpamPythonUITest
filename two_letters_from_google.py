import pytest
from selenium import webdriver
import selenium
from datetime import datetime
from home_page import HomePage
from hamcrest import assert_that, contains_string, equal_to
# import allure


mail_name1 = 'epamtestemail1@gmail.com'
pass1 = 'Ac1234567890'
mail_name2 = 'epamtestemail2@gmail.com'
pass2 = 'Ac1234567890xA'
date = datetime.strftime(datetime.now(), "%Y.%m.%d")


class Test2GoogleLetters:
    @pytest.yield_fixture(scope='session')
    def driver(self):
        # Before starting the test, copy chromedriver from http: // www.seleniumhq.org / download / and enter correct PATH.!!
        driver = selenium.webdriver.Chrome("D:\\downloads\\avtotests\\chromedriver.exe")
        driver.implicitly_wait(180)
        driver.fullscreen_window()
        yield driver
        driver.quit()

    def test_send_letters(self, driver):
        browser_name = driver.name
        text_mail = date + ' ' + browser_name

        homepage = HomePage(driver)
        homepage.login(mail_name1, pass1)
        homepage.send_mail(mail_name2, text_mail)
        homepage.move_to_sending_email()

        send_to_name = driver.find_element_by_name('epamtestemail2').text
        mail_text = driver.find_element_by_xpath("//div[contains(text(),'2019.02.10 chrome')]").text
        mail_name = driver.find_element_by_xpath("//h2[@class='hP']").text

        assert_that(mail_name, equal_to("Test"))
        assert_that(send_to_name, contains_string('epamtestemail2'))
        assert_that(mail_text, equal_to(text_mail))

        homepage.logout()
        homepage.login(mail_name2, pass2)
        homepage.click_to_incoming_message()

        # send_from_name = driver.find_element_by_name('epamtestemail2').text
        # assert_that(mail_name, equal_to("Test"))
        # assert_that(send_from_name, contains_string('epamtestemail2'))
        # assert_that(mail_text, equal_to(text_mail))




