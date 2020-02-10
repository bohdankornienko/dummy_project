import os
import sys

from datetime import datetime


if 'linux' == sys.platform:
    print('Registering repository for Linux system...')

    this_file = os.path.abspath(__file__)
    print('This file absolute path:', this_file)
    this_dir = os.path.split(this_file)[0]
    print('This file directory:', this_dir)

    home = os.environ['HOME']
    bashrc = os.path.join(home, '.bashrc')

    with open(bashrc, 'r') as fp:
        content = fp.readlines()

    pythonpath_update = 'export PYTHONPATH={}:$PYTHONPATH\n'.format(this_dir)

    now = datetime.now()
    date_comment = '# Automatically added by init.py on: {}'.format(now.strftime("%Y-%m-%d %H:%M:%S"))

    content += [date_comment, '\n', pythonpath_update, '\n']

    print('Appending .bashrc...')
    with open(bashrc, 'w') as fp:
        fp.writelines(content)

    print('Registration complete.')
