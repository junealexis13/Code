import time
import pynput

from pynput.mouse import Button, Controller    

ms = Controller()

while True:
    time.sleep(1)
    print(f'The mouse position is: {0}'.format(ms.position))