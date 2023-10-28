from pynput import mouse
from datetime import datetime


click_count = 0


#функция, вызываемая при клике мыши
def ClickHandler(x, y, button, pressed):
    global click_count
    time = datetime.now().time()
    if pressed:
        click_count += 1
        print(f'*click* {click_count}, {time}')

    if button == mouse.Button.right:
        return False 


listener = mouse.Listener(on_click=ClickHandler)

listener.start()
try:
    listener.join()
finally:
    print(f'listener stoped. click: {click_count}')
    listener.stop()