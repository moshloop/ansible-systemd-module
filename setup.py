from setuptools import setup
import os
import os.path
import re
import sys
from distutils.sysconfig import get_python_lib

nesting = len(re.findall('/', get_python_lib()))
prefix = '../' * nesting
HOME = os.getenv('HOME')
USER = HOME + '/.ansible/plugins/modules'
GLOBAL = '/usr/share/ansible/plugins/modules'

if not os.path.isdir(GLOBAL):
    try:
        os.makedirs(GLOBAL)
        DEST = GLOBAL
    except:
        print("Failed to create %s installing to %s" % (GLOBAL, USER), file=sys.stderr)
        DEST = USER
else:
    DEST = GLOBAL

setup(
    name = 'ansible-systemd-module', version = '1.1',
    url = 'https://www/github.com/moshloop/ansible-systemd-module',
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com',
    data_files=[
        (prefix + DEST, ['systemd_service.py'])
        ]
    )