import re
import dbus


class XFKeysMpris():
    """Instance for MPRIS2"""

    def __init__(self):
        self.bus = dbus.SessionBus()

    def get_player(self):
        """Check the name of the player running"""
        for service in self.bus.list_names():
            if re.match('org.mpris.MediaPlayer2.', service):
                player = dbus.SessionBus().get_object(
                    service, '/org/mpris/MediaPlayer2')
                interface = dbus.Interface(
                    player, dbus_interface='org.mpris.MediaPlayer2.Player')
                break
        else:
            return None
        return interface

    def toggle(self):
        """Toggle mpris play or pause"""
        if self.get_player():
            self.get_player().PlayPause()

    def play(self):
        if self.get_player():
            self.get_player().Play()

    def stop(self):
        """Stop mpris play"""
        if self.get_player():
            self.get_player().Stop()

    def prev(self):
        """Play previous song mpris"""
        if self.get_player():
            self.get_player().Previous()

    def next(self):
        """Play next song mpris"""
        if self.get_player():
            self.get_player().Next()
