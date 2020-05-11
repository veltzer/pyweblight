import datetime
import os
import socket

from config.helpers import help_check_output

general_current_folder = os.path.basename(os.getcwd())
general_current_year = datetime.datetime.now().year
general_homedir = os.path.expanduser('~')
# d.general_hostname=subprocess.check_output(['hostname']).decode().rstrip()
general_hostname = socket.gethostname()
general_domain_name = help_check_output(['hostname', '--domain']).rstrip()
