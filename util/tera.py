import pickle

from selenium.webdriver.common.by import By
from time import sleep


def login(driver):
    driver.get("https://www.terabox.com/vietnamese/")
    if 'main' not in driver.current_url:
        login_xpath = "//*[@id=\"app\"]/div/div/div[1]/div[4]/div/div[2]/div/div[2]/div/div[1]"
        driver.find_element(By.XPATH, login_xpath).click()
    else:
        pass


def get_cookie(driver):
    driver.get(driver.current_url)
    sleep(10)
    cookie = driver.get_cookie('ndus')
    value = 'ndus=' + cookie.get('value')
    return value
    #get all cookies
    # cookies = driver.get_cookies()
    # for cookie in cookies:
    #     name = cookie.get('name')
    #     value = cookie.get('value')




