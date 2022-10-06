import sys
import common.constant as Constant

from util import tera
from util.profile import ChromeProfile
from util.log import log_error, setup_logging
from util.test import TeraBox
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
        tera = TeraBox("D:\\test.txt", '123')
        tera.login()
        tera.upload_commit()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        log_error(e, is_critical=True)

