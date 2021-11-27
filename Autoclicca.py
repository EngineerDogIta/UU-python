#!/usr/bin/python3
from pyautogui import position, click
from time import sleep


def main():
    print("Press enter to continue")
    print("And move the mouse to the desired position")
    input()

    sleep(1)
    print("Caturing position in 3")
    sleep(1)
    print("Caturing position in 2")
    sleep(1)
    print("Caturing position in 1")
    pos = position()
    print("Got the mouse position in " + str(pos))

    n_times = int()
    while(not n_times > 0):
        print("Insert the number of times to click")
        try:
            n_times = int(input())
        except Exception:
            print("Not a valid number insert a valid number")

    time_to_wait = int()
    while(not time_to_wait > 0):
        print("Insert the time to wait between each click > 0")
        try:
            time_to_wait = int(input())
        except Exception:
            print("Not a valid number insert a valid number")

    start_with_click = str()
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
    for i in range(0, n_times):
        if(start_with_click.upper() == 'Y'):
            print("[" + str(i + 1) + "] clicked")
            click(pos)

        print("[" + str(i + 1) + "] waiting 1/2")
        sleep(time_to_wait / 2)
        print("[" + str(i + 1) + "] waiting 2/2")
        sleep(time_to_wait / 2)

        if(start_with_click.upper() == 'N'):
            print("[" + str(i + 1) + "] clicked")
            click(pos)
    print("Finish")
    sleep(4)


if __name__ == '__main__':
    main()
