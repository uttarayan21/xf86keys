# xf86keys

Same tool written in rust [mctl](https://github.com/uttarayan21/mctl-rs).  
I hope to add more features to it.
This will not recieve any more updates.

[python-mpd2](https://pypi.org/project/python-mpd2) is used for controlling [mpd](https://www.musicpd.org)  
[python-dbus](https://pypi.org/project/dbus-python) is used for controlling mpris  
[python-pynput](https://pypi.org/project/pynput) is used to monitor keystrokes

## Bugs:

- [x] The mpd client connection dies out on a long wait  
       I think it's fixed now (Check for the connection to mpd before any command)

## To do :

- [x] argparse to read arguments form commandline
- [x] Complete the mpdclient functions
- [x] Add mpris musicplayer control via python-dbus

# How to install:

- ## _ArchLinux_

  Install required packages

  ```bash
  sudo pacman -S python3 python-mpd2 python-dbus
  yay -S python-pynput
  ```

  then do

  ```bash
  git clone https://github.com/uttarayan21/xf86keys
  cd xf86keys
  git checkout PKGBUILD
  makepkg -si
  ```

  to build and install

- ## _Other distributions_

  If your package manager has the packages get from there or from pip

  ```bash
  sudo pip install dbus-python python-mpd2 pynput
  ```
