import time
import pynput

from pynput.mouse import Button as bt
from pynput.keyboard import Key

kb = pynput.keyboard.Controller()
ms = pynput.mouse.Controller()


if __name__ == "__main__":
    time.sleep(3)

    text = 'Hello World!'

    for x in text:
        kb.type(x)
        time.sleep(0.1)

