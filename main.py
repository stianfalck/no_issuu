from PIL import Image  # install by > python3 -m pip install --upgrade Pillow  # ref. https://pillow.readthedocs.io/en/latest/installation.html#basic-installation
import pyautogui as gui
import time
import keyboard
import cv2
import os

"""
# https://stackoverflow.com/questions/27327513/create-pdf-from-a-list-of-images

# 'The best method to convert multiple images to PDF I have tried so far is to use PIL purely.
# It's quite simple yet powerful:

# Just set save_all to True and append_images to the list of images which you want to add.

# You might encounter the AttributeError: 'JpegImageFile' object has no attribute 'encoderinfo'. 
# The solution is here Error while saving multiple JPEGs as a multi-page PDF

# Note:Install the newest PIL to make sure save_all argument is available for PDF.'

images = [
    Image.open("/Users/apple/Desktop/" + f)
    for f in ["bbd.jpg", "bbd1.jpg", "bbd2.jpg"]
]

pdf_path = "/Users/apple/Desktop/bbd1.pdf"

images[0].save(
    pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
"""

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