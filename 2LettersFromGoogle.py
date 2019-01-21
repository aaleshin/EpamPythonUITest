import selenium
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Before starting the test, copy chromedriver from http: // www.seleniumhq.org / download / and enter correct PATH.!!

mailname1 = 'epamtestemail1@gmail.com'
pass1 = 'Ac1234567890'

mailname2 = 'epamtestemail2@gmail.com'
pass2 = 'Ac1234567890xA'

driver = selenium.webdriver.Chrome("D:\\downloads\\avtotests\\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()



# driver.get("https://planner-sandbox.dev.thumbtack.net")
# driver.find_element_by_css_selector('#id_username').send_keys('gerardkunze')
# driver.find_element_by_css_selector('#id_password').send_keys('123456')
# driver.find_element_by_tag_name('button').click()
# driver.find_element_by_xpath('//a[@class="navbar__link"]//span[@class="avatar avatar_size_m"]').click()
# driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[2]/ul/li[4]/a').click()
# driver.find_element_by_css_selector('div.buttons_wrapper > div > a').click()
# WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="form"]/div[1]/div/div[1]/div/div[1]/select')))
# driver.find_element_by_css_selector('div.modal-body > div > div.vacation-type-block.row > div > div.vacation-type-select > select').click()
# driver.find_element_by_xpath('//*[@id="form"]/div[1]/div/div[1]/div/div[1]/select/option[5]').click()
# actions = ActionChains(driver).send_keys(Keys.ENTER).perform()


driver.quit()
