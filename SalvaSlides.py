import os, time, pyautogui

def main():

    print('How many slides??')
    print('--> insert a number <--')
    n_slides = int(input())
    print('How you want to call the slides?')
    name_slides = str(input())
    print('First be sure to be at the first of the {} slides'.format(n_slides))
    print('You\'ve got 5 seconds to check, if not just press ctrl-c to stop the terminal')
    print('or just get the mouse to the top left corner of the screen, the process will stop')

    time.sleep(5)
    # Create the folder if not exists
    screenshots_dir = "Screenshots"
    print('Screenshots will be saved in the folder {}'.format(screenshots_dir))
    if not os.path.exists(name_slides):
        os.makedirs(name_slides)
        print('Folder {} created'.format(name_slides))

    for i in range(n_slides):
        pyautogui.moveTo(2,2)
        slide_file_name = '{}{}{}_{}.png'.format(screenshots_dir, os.pathsep, name_slides, i)
        pyautogui.screenshot(slide_file_name, region=(357, 199, 772, 433))
        time.sleep(0.5)
        pyautogui.click(1100, 600)
        time.sleep(3)
        pyautogui.click(1100, 600)
        time.sleep(0.5)
    print("Finished!")

if __name__ == '__main__':
    main()