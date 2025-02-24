from PIL import Image 
import pyautogui as gui
import time
import keyboard
import cv2
import os


# mouse_positions = []
#
# for pos in range(10):
#     print(gui.position())
#     mouse_positions.append(gui.position())
#     time.sleep(1)



CONFIDENCE = 0.64

IMAGES_SAVE_PATH = "book"
PDF_SAVE_PATH = os.path.join("pdf", "Militær Atlet Protokol - Temahæfte.pdf")

arrow_cords = []

images = []

def locate_button():

    try:
        arrow_found = gui.locateOnScreen("right_arrow.png", confidence=CONFIDENCE)
        print(arrow_found[0], arrow_found[1])

        arrow_cords.append(arrow_found[0])
        arrow_cords.append(arrow_found[1])

    except gui.ImageNotFoundException:
        pass


def move_cursor_to_button():
    gui.moveTo(arrow_cords[0], arrow_cords[1])


def take_screenshots():
    img = gui.screenshot(region=(256, 24, 2303 - 256, 1464 - 24))


    filename = os.path.join(IMAGES_SAVE_PATH, f"page{i}.png")
    img.save(filename)
    return img

locate_button()

for i in range(46):
    images.append(take_screenshots())
    move_cursor_to_button()
    gui.click(button="left")
    time.sleep(0.5)

images[0].save(PDF_SAVE_PATH, "PDF", resolution=100, save_all=True, append_images=images[1:])
