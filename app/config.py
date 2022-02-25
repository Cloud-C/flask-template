import os
from configparser import ConfigParser

_current_path = os.path.dirname(os.path.abspath(__file__))

_config = ConfigParser()
_config.read(f'{_current_path}/config.ini')


class Config:
    HOST = _config['APP']['HOST']
    PORT = _config['APP'].getint('PORT')
    DEBUG = _config['APP'].getboolean('DEBUG')
