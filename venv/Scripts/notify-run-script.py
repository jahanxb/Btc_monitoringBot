#!e:\PycharmProjects\BitAddressMonitorBot\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'notify-run==0.0.12','console_scripts','notify-run'
__requires__ = 'notify-run==0.0.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('notify-run==0.0.12', 'console_scripts', 'notify-run')()
    )
