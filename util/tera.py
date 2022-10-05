import sys

from selenium.webdriver.common.by import By
from time import sleep
import common.constant as Constant
from util.log import log_error
from util.profile import ChromeProfile


def login(driver):
    driver.get("https://www.terabox.com/vietnamese/")
    if 'main' not in driver.current_url:
        login_xpath = "//*[@id=\"app\"]/div/div/div[1]/div[4]/div/div[2]/div/div[2]/div/div[1]"
        driver.find_element(By.XPATH, login_xpath).click()
    else:
        pass


def get_cookie(driver):
    driver.get(driver.current_url)
    sleep(Constant.WAIT_RELOAD)
    cookie = driver.get_cookie('ndus')
    value = 'ndus=' + cookie.get('value')
    return value





