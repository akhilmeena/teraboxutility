import sys
import common.constant as Constant

from time import sleep
from util.profile import ChromeProfile
from util.log import log_error, setup_logging

setup_logging()


def greet():
    # TODO-dung: add greeting
    pass


if __name__ == '__main__':
    greet()
    Constant.init()
    try:
        email = Constant.env["EMAIL"]
        email = email.split(':')
        profile = ChromeProfile(email[0], email[1], email[2])
        driver = profile.retrieve_driver()
        profile.start()
        # TODO-dung: continue here to get cookie + tera box token
        driver.get("https://www.google.com/")
        sleep(10)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        log_error(e, is_critical=True)

