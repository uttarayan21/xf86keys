#!/usr/bin/env python3
""" A pyhton script that controls both mpd and mpris music players """
# Trying to make a project which will control both playerctl and mpd
# media players so that one keybind can control it all
import os
import sys
import signal
import re
from configparser import ConfigParser
import dbus
from pynput import keyboard
from mpd import MPDClient

xf86_play = 269025044
xf86_stop = 269025045
xf86_prev = 269025046
xf86_next = 269025047

def signal_handler(signum, frame):
    log_it('\nInterrupted...')
    log_it('\nContinuing...')
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def log_it(string):
    log_file = os.path.expanduser('~') + '/.cache/xf86keys.log'
    if sys.stdin.isatty():
        print(string + '\n')
    else:
        with open(log_file, 'a+') as log:
            log.write(string + '\n')


def true():
    """Always returns true"""
    return True
class XFKeysMpris():
    """Instance for MPRIS2"""
    def __init__(self):
        self.bus = dbus.SessionBus()
    def get_player(self):
        """Check the name of the player running"""
        for service in self.bus.list_names():
            if re.match('org.mpris.MediaPlayer2.', service):
                player = dbus.SessionBus().get_object(service, '/org/mpris/MediaPlayer2')
                interface = dbus.Interface(player, dbus_interface='org.mpris.MediaPlayer2.Player')
                return interface
        else:
            return False
    def toggle(self):
        if self.get_player():
            self.get_player().PlayPause()
    def stop(self):
        if self.get_player():
            self.get_player().Stop()
    def prev(self):
        if self.get_player():
            self.get_player().Previous()
    def next(self):
        if self.get_player():
            self.get_player().Next()


class XFKeysMpd():
    """ The instance for controlling the mpd player"""

    def __init__(self, host, port, timeout, idletimeout):

        self.client = MPDClient()
        self.client.timeout = timeout
        self.client.idletimeout = idletimeout
        try:
            self.client.connect(host, port)
        except ConnectionRefusedError:
            log_it('Connection Failed')
            log_it(' If you run mpd server in other than {}:{} \
                then please edit the config file'.format(host, port))
            raise SystemExit

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

def read_config(config_path):
    host = 'localhost'
    port = 6600
    timeout = 10
    idletimeout = None
    config = ConfigParser()
    if not os.path.isfile(config_path):
        log_it('Config couldn\'t be read')
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

    return [host, port, timeout, idletimeout]

def main():
    """ executed when called as __init__ """
    # Description and variables
    # about = """A client to control both MPRIS and MPD playbacks.
    #         Made this to control keybinds of media keys"""
    # helpmsg = """
    # Play the music from either
    # MPRIS or MPD which ever was played last"""
    config_path = os.path.expanduser('~') + '/.config/xf86keys.conf'

    try:
        # mpd_client = XFKeysMpd(host, port, 10, None)
        mpd_client = XFKeysMpd(*read_config(config_path))
    except NameError:
        log_it('Unkown Error: Please check the config file')
    try:
        mpris_client = XFKeysMpris()
    except NameError:
        log_it('Unkown Error: Please open a issue in the github repo')

    if mpd_client.is_playing():
        client = mpd_client
    else:
        client = mpris_client

    def call_func(call_key):
        """Dictionary to call functions"""
        key_event_map = {
            keyboard.KeyCode.from_vk(xf86_play): client.toggle,
            keyboard.KeyCode.from_vk(xf86_stop): client.stop,
            keyboard.KeyCode.from_vk(xf86_next): client.next,
            keyboard.KeyCode.from_vk(xf86_prev): client.prev,
        }
        return key_event_map.get(call_key, true)


    def on_press(key):
        """Call the dictionary on any key press"""
        call_func(key)()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == '__main__':
    main()
