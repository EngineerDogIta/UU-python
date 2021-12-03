#!/usr/bin/python3
import pyautogui
from random import randint
from time import sleep
import sys
import os


def invalidarguments(argument: str):
    print("Error: " + argument)
    print(
        "Usage: python3 Autoclicca.py [number of clicks] [delay between clicks] [start with click? Y/N]")
    print("Example: python3 Autoclicca.py 10 0.1")


def validate_n_clicks(n_clicks: int):
    if(n_clicks < 1):
        invalidarguments("Invalid number of clicks")
        exit()


def validate_seconds_delay(seconds_delay: int):
    if(seconds_delay < 0):
        invalidarguments("Invalid delay of seconds")
        exit()


def click_mouse(index: int, position: pyautogui.Point):
    print(f"[{index + 1}] clicked")
    pyautogui.click(position)


def validate_image2click(image2click: str):
    # check if file exists
    if(image2click != ""):
        if(not os.path.isfile(image2click)):
            # check if it is a valid image
            if(not image2click.endswith(".png")):
                invalidarguments("Invalid image file")
                exit()
            invalidarguments("Image not found")
            exit()

    if(image2click == ""):
        invalidarguments("[image to click]")
        exit()


def main():
    n_clicks = int()
    seconds_delay = int()
    start_with_click = str()
    image_button2click = str()
    if (len(sys.argv) >= 2):
        # if first argument exists
        if (sys.argv[1] == "--help"):
            print("Usage: python3 Autoclicca.py [number of clicks] [delay between clicks]")
            print("Example: python3 Autoclicca.py 10 0.1")
            print("This will click 10 times with a delay of 0.1 seconds between each click")
            exit()
        if (sys.argv[1].isdigit()):
            # if first argument is a number
            n_clicks = int(sys.argv[1])
        else:
            invalidarguments('[number of clicks]')

        # if second argument exists
        if (len(sys.argv) >= 3):
            if (sys.argv[2].isdigit()):
                seconds_delay = int(sys.argv[2])
            else:
                invalidarguments('[number of clicks] [delay between clicks]')
            # if third argument exists
            if (len(sys.argv) >= 4):
                if(start_with_click.upper() not in ("Y", "N")):
                    invalidarguments('[start with click? Y/N]')
                start_with_click = str(sys.argv[3])
                # if fourth argument exists
                if (len(sys.argv) >= 5):
                    validate_image2click(sys.argv[4])
                    image_button2click = str(sys.argv[4])



    pyautogui.FAILSAFE = True
    print("Press enter to continue")
    print("And move the mouse to the desired position")
    input()

    sleep(1)
    print("Caturing position in 3")
    sleep(1)
    print("Caturing position in 2")
    sleep(1)
    print("Caturing position in 1")
    pos = pyautogui.position()
    print("Got the mouse position in " + str(pos))

    while(not n_clicks.isdigit() and n_clicks < 1):
        print("Insert the number of times to click")
        try:
            n_clicks = int(input())
        except Exception:
            print("Not a valid number insert a valid number")

    while(not seconds_delay.isdigit() and seconds_delay < 0):
        print("Insert the time to wait between each click > 0")
        try:
            seconds_delay = int(input())
        except Exception:
            print("Not a valid number insert a valid number")

    while(start_with_click.upper() not in ("Y", "N")):
        print("Start with the click? [Y/N]")
        start_with_click = str(input())
        if(start_with_click.upper() not in ("Y", "N")):
            print("Input not valid, use characters Y or N, ignores case")

    print("starting, 3 sec wait")
    sleep(1)
    print("starting, 2 sec wait")
    sleep(1)
    print("starting, 1 sec wait")
    sleep(1)

    print("Start")
    for i in range(0, n_clicks):
        if(image_button2click != ""):
            pos = pyautogui.locateCenterOnScreen(image_button2click)

        if(start_with_click.upper() == 'Y'):
            print("[" + str(i + 1) + "] clicked")
            pyautogui.click(pos)

        print("[" + str(i + 1) + "] waiting 1/2")
        pyautogui.moveTo(randint(600, 1200), randint(600, 1200), )
        sleep(seconds_delay / 2)

        print("[" + str(i + 1) + "] waiting 2/2")
        pyautogui.moveTo(randint(600, 1200), randint(600, 1200))
        sleep(seconds_delay / 2)

        if(start_with_click.upper() == 'N'):
            print("[" + str(i + 1) + "] clicked")
            pyautogui.click(pos)
    print("Finish")
    sleep(4)


if __name__ == '__main__':
    main()
