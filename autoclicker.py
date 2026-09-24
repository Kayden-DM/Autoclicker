from pynput import mouse, keyboard
import threading
import time

clicking = False
mouse_controller = mouse.Controller()

def autoclick():
    global clicking

    while True:
        if clicking:

            mouse_controller.click(mouse.Button.left)
            time.sleep(0.001)
        else:
            time.sleep(0.01)
        

def on_press(key):
    global clicking

    try:
        if key.char == 's':
            clicking = not clicking
            print("Auto clicker" , "ON" if clicking else "OFF")
    except AttributeError:
        pass


threading.Thread(target=autoclick, daemon=True).start()


print("Press 's' to start/stop the autoclick. ")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()