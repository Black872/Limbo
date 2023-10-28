from pynput import mouse


click_count = 0


#функция, вызываемая при клике мыши
def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1
        print(f'Клик {click_count}')

        if click_count >= 10:  #остановка прослушивания после 10 кликов
            listener.stop()
            
#объект слушателя мыши
listener = mouse.Listener(on_click=on_click)


listener.start()


listener.join()