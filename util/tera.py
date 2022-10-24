import requests
import os
import pyzipper
from cryptography.fernet import Fernet
from selenium.webdriver.common.by import By
import common.constant as Constant
from util.profile import ChromeProfile
import zipfile
import shutil


class TeraBox:

    def __init__(self, path):
        email = Constant.env["EMAIL"]
        email = email.split(':')
        profile = ChromeProfile(email[0], email[1], email[2])
        self.driver = profile.retrieve_driver()
        self.path = path
        self.copy_path = self.path.split(".")[0] + '_copy'
        self.file_type = Constant.env["FILE_TYPE"]
        self.zip_path = self.path.split(".")[0] + self.file_type
        profile.start()
        self.login()
        self.cookie = self.get_cookie()
        self.zip_directory()

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

    def upload_file(self, path_zip):
        url_upload = 'https://c-jp.terabox.com/rest/2.0/pcs/superfile2'
        app_id = int(Constant.env["APP_ID"])
        params = {
            'method': 'upload',
            'app_id': app_id,
            'path': '/abc.txt',
            'uploadid': 'N1-MTQu',
            'partseq': 0
        }
        headers = {
            'Cookie': self.cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/105.0.0.0 Safari/537.36',
        }
        files = {'file': open(path_zip, 'rb')}
        try:
            response = requests.post(url=url_upload, params=params, headers=headers, files=files)
            result = response.json()["md5"]
            return result
        except:
            print('Error')

    def upload(self):
        path = self.zip_path
        size = os.stat(path=path).st_size
        file_name = os.path.basename(path).split('/')[-1]
        md5 = self.upload_file(path_zip=path)
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

        requests.post(url=url, headers=headers, data=data)
        self.delete(self.zip_path)

    def zip_file(self):
        try:
            with pyzipper.AESZipFile(self.zip_path,
                                     'w',
                                     compression=pyzipper.ZIP_LZMA) as zf:
                zf.write(filename=self.path)
                return zf.filename
        except:
            pass

    @staticmethod
    def encrypt_file(file_path):
        key = Constant.env["KEY"]
        key = key.encode('utf-8')
        fernet = Fernet(key)
        with open(file_path, 'rb') as file:
            original = file.read()

        encrypted = fernet.encrypt(original)
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def zip_directory(self):
        self.copy_directory()
        with zipfile.ZipFile(self.zip_path, mode='w') as zipf:
            len_dir_path = len(self.path)
            for root, _, files in os.walk(self.copy_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    self.encrypt_file(file_path=file_path)
                    zipf.write(file_path, file_path[len_dir_path:])
        self.delete(self.copy_path)

    def copy_directory(self):
        shutil.copytree(self.path, self.copy_path)

    @staticmethod
    def delete(path):
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
        elif os.path.isdir(path):
            shutil.rmtree(path)
        else:
            raise ValueError("Path {} is not a file or dir.".format(path))
