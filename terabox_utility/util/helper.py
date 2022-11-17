import os
import shutil
import zipfile
import time
from cryptography.fernet import Fernet


def encrypt_file(file_path, key):
    k = key.encode('utf-8')
    fernet = Fernet(k)
    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def delete(path):
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        raise ValueError("Path {} is not a file or dir.".format(path))


def unzip(in_path, out_path):
    with zipfile.ZipFile(in_path, "r") as zip_ref:
        zip_ref.extractall(out_path)


def decrypt(path, key):
    k = key.encode('utf-8')
    fernet = Fernet(k)
    with open(path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(path, 'wb') as dec_file:
        dec_file.write(decrypted)


def download_wait(directory):
    """
    Wait for downloads.

    Args
    ----
    directory : str
        The path to the folder where the files will be downloaded.

    """
    dl_wait = True
    while dl_wait:
        time.sleep(15)
        dl_wait = False
        files = os.listdir(directory)
        for fname in files:
            if fname.endswith('.crdownload'):
                dl_wait = True
