import os
import sys
import signal
import argparse
from pynput import keyboard
from xf86keys.xlog import log_it
from xf86keys.xmpd import XFKeysMpd
from xf86keys.xmpris import XFKeysMpris
from xf86keys.xconfig import read_config


xf86_play = 269025044
xf86_stop = 269025045
xf86_prev = 269025046
xf86_next = 269025047


def sig_handler(signum, _frame):
    """SIgnal Handler"""
    if signum == signal.SIGINT:
        log_it('\nSIGINT Interrupt recieved...\nExitting...')
        raise SystemExit
    log_it('\nInterrupted...\nSend SIGINT to kill')


signal.signal(signal.SIGINT, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)


def daemonize(mpd_client, mpris_client):
    key_list = [keyboard.Key.media_play_pause, keyboard.Key.media_next,
                keyboard.Key.media_previous, keyboard.KeyCode.from_vk(269025045)]

    def call_func(call_key):
        """Dictionary to call functions"""
        mpd_client.check_connect()
        if mpd_client.is_playing():
            client = mpd_client
        else:
            client = mpris_client
        key_event_map = {
            # keyboard.KeyCode.from_vk(xf86_play): client.toggle,
            keyboard.Key.media_play_pause: client.toggle,
            keyboard.KeyCode.from_vk(xf86_stop): client.stop,
            # keyboard.KeyCode.from_vk(xf86_next): client.next,
            keyboard.Key.media_next: client.next,
            # keyboard.KeyCode.from_vk(xf86_prev): client.prev,
            keyboard.Key.media_previous: client.prev,

        }
        return key_event_map.get(call_key, lambda: True)

    def handle(key):
        """Call the dictionary on any key press"""
        try:
            if key in key_list:
                call_func(key)()
        except AttributeError:
            pass

    with keyboard.Listener(on_press=handle) as listener:
        listener.join()


def main():
    parser = argparse.ArgumentParser(
        description="Control Both mpd and mpris media players at the same time using media keys")
    group = parser.add_mutually_exclusive_group(required=True)

    parser.add_argument(
        "-p", "--player", choices=["mpris", "mpd"], help="Explicitly specify the music player to use")
    group.add_argument(
        '-d', '--daemon', help="Run as a daemon using pynput to monitor keys", action='store_true')
    group.add_argument("action", choices=[
        "play", "pause", "toggle", "prev", "next", "stop"], nargs='?', help="Play, pause, toggle, previous, next or stop the music player")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)
    args = parser.parse_args()

    config_path = os.path.expanduser('~') + '/.config/xf86keys.conf'
    config = read_config(config_path)
    try:
        mpd_client = XFKeysMpd(config)
    except NameError:
        log_it('Unkown Error: Please check the config file')
    try:
        mpris_client = XFKeysMpris()
    except NameError:
        log_it('Unkown Error: Please open a issue in the github repo')

    if args.daemon:
        # if os.fork() == 0:
        daemonize(mpd_client, mpris_client)
    else:
        if mpd_client.is_playing():
            client = mpd_client
        else:
            client = mpris_client
        eval(f"client.{args.action}()")  # Please don't kill me I'm lazy


if __name__ == '__main__':
    main()
