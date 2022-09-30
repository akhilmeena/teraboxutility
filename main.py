import sys
import common.constant as Constant

from time import sleep

from util import tera
from util.profile import ChromeProfile
from util.log import log_error, setup_logging

setup_logging()


def greet():
    str = ("████████╗███████╗██████╗░░█████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗████████╗██╗██╗░░░░░██╗████████╗██╗░░░██╗\n"
    "╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝██║░░░██║╚══██╔══╝██║██║░░░░░██║╚══██╔══╝╚██╗░██╔╝\n"
    "░░░██║░░░█████╗░░██████╔╝███████║██████╦╝██║░░██║░╚███╔╝░██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░░╚████╔╝░\n"
    "░░░██║░░░██╔══╝░░██╔══██╗██╔══██║██╔══██╗██║░░██║░██╔██╗░██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░░░╚██╔╝░░\n"
    "░░░██║░░░███████╗██║░░██║██║░░██║██████╦╝╚█████╔╝██╔╝╚██╗╚██████╔╝░░░██║░░░██║███████╗██║░░░██║░░░░░░██║░░░\n"
    "░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░\n")
    print(str)



if __name__ == '__main__':
    greet()
    Constant.init()
    try:
        email = Constant.env["EMAIL"]
        email = email.split(':')
        profile = ChromeProfile(email[0], email[1], email[2])
        driver = profile.retrieve_driver()
        profile.start()
        tera.login(driver)
        ndus = tera.get_cookie(driver)
        print(ndus)
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        log_error(e, is_critical=True)

