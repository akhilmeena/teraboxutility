from time import sleep

import requests

import common.constant as Constant
from selenium.webdriver.common.by import By
import json


class TeraBox:
    def __init__(self, profile):
        self.driver = profile.retrieve_driver()
        # profile.start()

    def login(self):
        self.driver.get("https://www.terabox.com/vietnamese/")
        if 'main' not in self.driver.current_url:
            login_xpath = "//*[@id=\"app\"]/div/div/div[1]/div[4]/div/div[2]/div/div[2]/div/div[1]"
            self.driver.find_element(By.XPATH, login_xpath).click()
        else:
            pass

    def get_cookie(self):
        self.driver.get(self.driver.current_url)
        cookie = self.driver.get_cookie('ndus')
        value = 'ndus=' + cookie.get('value')
        return value

    def upload_file(self):
        url_upload = 'https://c-jp.terabox.com/rest/2.0/pcs/superfile2'
        params = {
            'method': 'upload',
            'app_id': 250528,
            'path': '/abc.txt',
            'uploadid': 'N1-MTQu',
            'partseq': 0
        }

        headers = {
            'Cookie': 'ndus=YbV8A6MteHuiH7sndvNB-hrVLtXPxD8dynOdsGYk',
            'Content-Type': 'text / html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        files = {'file': open("D:\\test.txt", 'rb')}
        print(type(files))
        response = requests.post(url=url_upload, params=params, headers=headers, data=files)
        print(response.json())
        print(response.status_code)
        print(response.url)
