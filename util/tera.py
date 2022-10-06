import requests
import os
import pyzipper

from selenium.webdriver.common.by import By
import common.constant as Constant
from util.profile import ChromeProfile


class TeraBox:

    def __init__(self, path, password):
        email = Constant.env["EMAIL"]
        email = email.split(':')
        profile = ChromeProfile(email[0], email[1], email[2])
        self.driver = profile.retrieve_driver()
        self.cookie = None
        self.path = path
        self.password = password
        profile.start()

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
        ndus = 'ndus=' + cookie.get('value')
        return ndus

    def upload_file(self):
        self.cookie = self.get_cookie()
        url_upload = 'https://c-jp.terabox.com/rest/2.0/pcs/superfile2'
        params = {
            'method': 'upload',
            'app_id': 250528,
            'path': '/adgvd.txt',
            'uploadid': 'N1-MTQu',
            'partseq': 0
        }
        path = self.zip_file()
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        }
        files = {'file': open(path, 'rb')}
        response = requests.post(url=url_upload, params=params, headers=headers, files=files)
        result = response.json()["md5"]
        return result

    def upload_commit(self):
        path = self.zip_file()
        size = os.stat(path=path).st_size
        file_name = os.path.basename(path).split('/')[-1]
        md5 = self.upload_file()
        self.cookie = self.get_cookie()
        url = 'https://www.terabox.com/api/create'
        headers = {
            'Cookie': self.cookie,
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'path': file_name,
            'size': size,
            'block_list': '["' + md5 + '"]'
        }

        response = requests.post(url=url, headers=headers, data=data)

    def zip_file(self):
        password = str.encode(self.password)
        zip_name = self.path.split(".")[0] + '.zip'
        with pyzipper.AESZipFile(zip_name,
                                 'w',
                                 compression=pyzipper.ZIP_LZMA,
                                 encryption=pyzipper.WZ_AES) as zf:
            zf.setpassword(password)
            zf.write(filename=self.path)
            return zf.filename








