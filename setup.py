
from subprocess import *
from setuptools import setup, find_packages
import os
import os.path

HOME = os.getenv('HOME')
USER = HOME + '/.ansible/plugins/modules'
GLOBAL = '/usr/share/ansible/plugins/modules'

if not os.path.isdir(GLOBAL):
    try:
        os.makedirs(GLOBAL)
        DEST=GLOBAL
    except:
        print("Failed to create %s installing to %s" % (GLOBAL, USER))
        DEST = USER
else:
    DEST=GLOBAL
setup(
    name = 'ansible-systemd-module', version = '1.0',
    url = 'https://www/github.com/moshloop/ansible-systemd-module',
    author = 'Moshe Immerman', author_email = 'firstname.surname@gmail.com',
    data_files=[
    (DEST, ['systemd_service.py'])
    ]
    )