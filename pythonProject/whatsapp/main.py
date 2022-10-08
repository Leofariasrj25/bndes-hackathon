import pyautogui as pt
from time import sleep
import cv2
import pyperclip
import random

sleep(3)

path = r"C:\Users\Mateus\PycharmProjects\pythonProject\whatsapp\emotes_paperclip.png"
path2 = r"C:\Users\Mateus\PycharmProjects\pythonProject\whatsapp\green_circle.png"
img = cv2.imread(path)
position1 = pt.locateOnScreen(img, confidence=.8)
x = position1[0]
y = position1[1]
i = 0
counter = 0


# gets message
def get_message():
    global x, y

    x = -1
    y = -1
    position = pt.locateOnScreen(img, confidence=.8)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=0.5)
    pt.moveTo(x + 25, y - 46, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    #print(whatsapp_message)

    return whatsapp_message



def post_response(message):
    global x, y

    position = pt.locateOnScreen(path, confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=0.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=0.5)


# process_response
def process_response(message, contador):

    if contador == 0:
        return "*Boas-vindas! Vamos fazer um pre-levantamento socioeconomico?*"
    if contador == 4:
        return "*Obrigado por participar!*"
    if contador == 1:
        return "Qual seu nome?"
    elif contador== 2:
        return "Qual seu CPF?"
    else:
        return "Qual sua renda bruta mensal?"


# check for new messages
def check_for_new_messages():
    global counter
    pt.moveTo(x+20, y-40, duration=.5)


    while True:

        try:
            position = pt.locateOnScreen(path2, confidence=0.7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(2)

        except(Exception):
            print("no new other users with new messages located")

        if pt.pixelMatchesColor(int(x+20), int(y-40), (255, 255, 255), tolerance=10):
            print("is_white")
            processed_message = process_response(get_message(), counter)
            post_response(processed_message)
            counter += 1
            if counter == 1:
                processed_message = process_response(get_message(), counter)
                post_response(processed_message)
            if counter == 5:
                return 0
        else:
            print("no new messages")
        sleep(5)

check_for_new_messages()
#
#while True:
 #   print(question)
 #   processed_message = process_response(get_message(), question)
 #   post_response(processed_message)
 #   question += 1
 #   if question == 4:
 #       break
