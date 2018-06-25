#!/usr/bin/env python3
""" A pyhton script that controls both mpd and mpris music players """
# Trying to make a project which will control both playerctl and mpd
# media players so that one keybind can control it all
import sys
import argparse
from mpd import MPDClient


def main():
    """ executed when called as __init__ """
    # Description and variables
    about = """A client to control both MPRIS and MPD playbacks.
            Made this to control keybinds of media keys"""
    helpmsg = """
    Play the music from either
    MPRIS or MPD which ever was played last"""

    class XFKeysMpd():
        """ The instance for controlling the mpd player"""

        def __init__(self, host, port, timeout, idletimeout):

            self.client = MPDClient()
            self.client.timeout = timeout
            self.client.idletimeout = idletimeout
            self.client.connect(host, port)

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
            self.client.pause()
    mpd_client = XFKeysMpd('localhost', 6600, 10, None)
    mpd_client.play()

    if len(sys.argv) <= 1:
        sys.argv.append('help')
    if sys.argv[1] == 'play':
        mpd_client.play()
    elif sys.argv[1] == 'pause':
        mpd_client.pause()
    elif sys.argv[1] == 'stop':
        mpd_client.stop()
    elif sys.argv[1] == 'toggle':
        mpd_client.toggle()
    elif sys.argv[1] == 'help':
        print(helpmsg)


if __name__ == '__main__':
    main()
