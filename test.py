from pynput import keyboard
from pynput.keyboard import Key, Controller

keyboard2 = Controller()

def on_activate1():
    #print('Global hotkey activated!')
    #print('Global hotkey activated!')
    keyboard2.press('v')
    keyboard2.release('v')
    keyboard2.press('e')
    keyboard2.release('e')
    keyboard2.press('l')
    keyboard2.release('l')


def on_activate2():
    #print('Global hotkey activated!')
    #print('Global hotkey activated!')
    keyboard2.press('v')
    keyboard2.release('v')
    keyboard2.press('e')
    keyboard2.release('e')
    keyboard2.press('j')
    keyboard2.release('j')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

#hotkey = keyboard.HotKey(
    #keyboard.HotKey.parse('<ctrl>+<alt>+h'),
    #keyboard.HotKey.parse('c'),
#    keyboard.HotKey.parse('<space>'),
#    on_activate)

#with keyboard.Listener(
#        on_press=for_canonical(hotkey.press),
#        on_release=for_canonical(hotkey.release)) as l:
#    l.join()

with keyboard.GlobalHotKeys({
        '<space>': on_activate1,
        'p': on_activate2}) as h:
    h.join()
