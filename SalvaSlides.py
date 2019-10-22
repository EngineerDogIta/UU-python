import time, pyautogui

print('How many slides??')
print('--> insert a number <--')
iSlides = int(input())
print('How do you wanna call the slides?')
nomeSlides = str(input())
print('First be sure to be at the first of the {} slides'.format(iSlides))
print('You\'ve got 5 seconds to check, if not just press ctrl-c to stop the terminal')
print('or just get the mouse to the top left corner of the screen, the process will stop')

time.sleep(5)

for i in range(iSlides):
    pyautogui.moveTo(2,2)
    pyautogui.screenshot("Modulo2Screenshots\\"+nomeSlides+str(i)+'.png', region=(357, 199, 772, 433))
    time.sleep(0.5)
    pyautogui.click(1100, 600)
    time.sleep(3)
    pyautogui.click(1100, 600)
    time.sleep(0.5)
print("FINITO!")
