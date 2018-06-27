#!/usr/bin/env python3

import os
#import 
from pynput import keyboard

def on_play(key):
#    if key == keyboard.KeyCode('269025044'):
#        os.system('mpc play')
#        print('mpc play')
    if key == keyboard.KeyCode.from_vk(269025044):
        print('FML')
    print('Are they even calling me ?')
with keyboard.Listener(
	on_press=on_play) as listener:
    listener.join()
