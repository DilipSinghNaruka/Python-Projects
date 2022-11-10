# I was searching for a simple solution without window focus. Jayk's answer, pynput, works perfect for me. Here is the example how I use it.

from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '2', 'left', 'right','z','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','p','o','i','u','y','t','r','e','w','q',]: 
     # keys of interest
        # self.keys.append(k)  # store it in global-like variable
       print('Key pressed: ' + k)
       return False  # stop listener; remove this if want more keys

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys 