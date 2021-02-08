import mpd
from xf86keys.xlog import log_it


class XFKeysMpd():
    """ The instance for controlling the mpd player"""

    def __init__(self, config):
        self.client = mpd.MPDClient()
        self.client.timeout = config.timeout
        self.client.idletimeout = config.idletimeout
        self.config = config
        try:
            self.client.connect(config.host, config.port)
        except ConnectionRefusedError as connection_error:
            log_it('Connection Failed')
            log_it(' If you run mpd server in other than {}:{} \
                then please edit the config file'.format(config.host, config.port))
            raise SystemExit from connection_error

    def check_connect(self):
        """Check the connection and re establish if disconnected"""
        config = self.config
        try:
            self.client.ping()
        except mpd.base.ConnectionError:
            log_it('ConnectionError ocurred')
            try:
                log_it('Trying to disconnect')
                self.client.disconnect()
            except mpd.base.ConnectionError:
                log_it('Disconnect failed')
            try:
                log_it('Trying to Reconnect')
                self.client.connect(config.host, config.port)
            except ConnectionRefusedError:
                log_it("Connection Refused")
                raise SystemExit('Connection Refused')

    def play(self):
        """ Play the song """
        self.client.play()

    def pause(self):
        """Pause the song """
        self.client.pause()

    def stop(self):
        """"Stop the song"""
        self.client.stop()

    def toggle(self):
        """Toggle play or pause"""
        if self.is_playing():
            self.client.pause()
        else:
            self.client.play()

    def next(self):
        """Play the next song"""
        if self.is_playing():
            self.client.next()

    def prev(self):
        """Play the prev song"""
        if self.is_playing():
            self.client.previous()

    def is_playing(self):
        """is the song playing"""
        if self.client.status()['state'] == 'stop':
            return False
        return True
