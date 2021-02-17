import os
from xf86keys.xlog import log_it
from configparser import ConfigParser


class Config:
    def __init__(self, host='localhost', port=6600, timeout=10, idletimeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.idletimeout = idletimeout


def read_config(config_path):
    """Read the config file and return mpd host and port"""
    # host = 'localhost'
    # port = 6600
    # timeout = 10
    # idletimeout = None
    config = ConfigParser()
    if not os.path.isfile(config_path):
        log_it('Config couldn\'t be read')
        log_it('Falling back to default values for them')
        return Config()
    else:
        config.read(config_path)
    try:
        host = config['MPD']['host']
    except KeyError:
        log_it('Host couldn\'t be read from config')
    try:
        port = config['MPD']['port']
    except KeyError:
        log_it('Port couldn\'t be read from config')
    try:
        port = config['MPD']['port']
    except KeyError:
        log_it('Port couldn\'t be read from config')

    return Config(host, port, timeout=10, idletimeout=None)
