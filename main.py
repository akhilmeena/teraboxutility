import os
import sys
import common.constant as Constant

from util.log import log_error, setup_logging
from util.tera import TeraBox

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
        a = ['terabox269@gmail.com:dung@123', 'autsaree1997@gmail.com:Ovlcicqjbslw54']
        tera = TeraBox(a)
        tera.get_all_dir()

    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        log_error(e, is_critical=True)
