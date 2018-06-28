# xf86keys

~Script to map media keys to~ this now runs as daemon and maps itself to media keys

The mpd control uses python-mpd2

Plannig to use python-dbus for the mpris

For keyboard mapping it uses python-pynput

Version: 1

# To do :
* ~argparse ... stuff~ FML ... I am a NOOB, Can't do this ... yet
* ~Complete the mpdclient functions~ Done
* ~Add mpris musicplayer control via python-dbus~ Done

# How to install:

* ## _ArchLinux_
```sudo pacman -S python3 python-mpd2 python-dbus```
for pynput you can get it from aur or pip

```git clone https://aur.archlinux.org/python-pynput```

```cd python-pynput```

```makepkg -si```

or from pip

```sudo pip install pynput```


* ## _Other distributions_
If your package manager has the packages get from there or from pip

```sudo pip install dbus-python python-mpd2 pynput```
