import time
from pynput import mouse
from datetime import datetime


click_count = 0


def handler():
    #функция, вызываемая при клике мыши
    def ClickHandler(x, y, button, pressed):
        global click_count
        time = datetime.now().time()
        if pressed:
            click_count += 1
            print(f'Клик {click_count}, {time}')

            if click_count >= 10:  #остановка отслеживание после 10 кликов
                listener.stop()
                l = False               
                
    #объект слушателя мыши
    listener = mouse.Listener(on_click=ClickHandler)

            
    listener.start()
    
    listener.join()


