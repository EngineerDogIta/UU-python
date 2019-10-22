import time, pyautogui

print('Quante sono le slides? conto anche quella del quiz tranq')
iSlides = int(input())
print('Come vuoi chiamarle le slides?')
nomeSlides = str(input())
print('Parto con lo scraping assicurati di trovarti alla prima delle {} slides'.format(iSlides))
print('Hai tempo 5 secondi poi parto')
print('per fermare il programma usa ctrl-z, ctrl-c o muovi il mouse in alto a sinistra dello schermo')

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