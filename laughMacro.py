from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard2 = Controller()

def on_activate():
    #print('Global hotkey activated!')
    keyboard2.press('v')
    keyboard2.release('v')
    keyboard2.press('e')
    keyboard2.release('e')
    keyboard2.press('l')
    keyboard2.release('l')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    #keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    #keyboard.HotKey.parse('c'),
    keyboard.HotKey.parse('<space>'),
    on_activate)

with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()
