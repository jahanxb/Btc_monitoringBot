#!E:\PycharmProjects\BitAddressMonitorBot\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'notify==0.3.1','console_scripts','notify'
__requires__ = 'notify==0.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('notify==0.3.1', 'console_scripts', 'notify')()
    )
