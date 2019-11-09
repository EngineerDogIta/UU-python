#!/usr/bin/python3
import random

'''
usando il crivello di Eratostene
possiamo trovare tutti i numeri primi compresi tra a e b
'''


def stampaprimi(a, b):
    numeri = range(a, b)
    for n in numeri:
        if isprimo(n) == True:
            print('il numero ' + str(n) + ' non e` primo')
        else:
            print('il numero ' + str(n) + ' è primo')


def isprimo(x):
    return not ((x % 2 == 0) | (x % 3 == 0) | (x % 5 == 0) | (x % 7 == 0))


def trovaprimi(a, b):
    return list(filter(lambda x: isprimo(x), list(range(a, b))))


def comandotrovaprimi():
    try:
        varia = input('inserisci un numero intero da cui partire per trovare i ' + 'numeri primi => ')
        while (int(varia) == 1 and int(varia) == 0):
            varia = input('il numero ' + str(
                varia) + ' non è identificabile come primo o multiplo \n' + 'inserire un numero intero valido => ')
    except Exception as e:
        varia = random.randint(10, 65535)
        print('qualcosa è andato storto scelgo un numero a caso ' + str(varia))
    finally:
        print('partenza da ' + str(varia))
    try:
        varib = input('inserisci un numero intero a cui arrivare per trovare i ' + 'numeri primi => ')
        while (int(varib) <= int(varia)):
            varib = input('attenzione il numero inserito è ' + varib + ' ed è minore di ' + str(varia) + '\n' + (
                    ' ' * 20) + ' inserire un numero più grande (consigliato ' + str(int(varia) + 1) + ') => ')
    except Exception as e:
        varib = random.randint(int(varia) + 1, 65535)
        print('qualcosa è andato storto scelgo un numero a caso ' + str(varib))
    finally:
        print('arrivo a ' + str(varia))
    print("inizio l'analisi")
    stampaprimi(int(varia), int(varib))


def comandoprimocasuale():
    a = random.randint(10, 65535)
    print(random.choice(trovaprimi(1, a)))


if __name__ == '__main__':
    esci = True
    while (esci):
        comando = input(
            "\n\nbenvenuto in cosa posso esserti utile?\n a) stampa tutti i numeri primi da una certa ampiezza\n b) "
            "stampa un numero primo casuale\n\n => ")
        if comando == 'a':
            comandotrovaprimi()
        elif comando == 'b':
            comandoprimocasuale()
        elif comando == 'e' or comando == 'esci' or comando == 'exit':
            esci = False
