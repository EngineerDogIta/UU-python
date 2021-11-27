#!/usr/bin/python3
import random

'''
Sieve of Eratosthenes
Using the Sieve of Eratosthenes, we can find all the prime numbers between 1 and n.
'''


def print_primes(a: int, b: int):
    numbers_range = range(a, b)
    [print('{} is a prime number'.format(x))
     for x in filter(lambda x: is_prime(x), numbers_range)]
    [print('{} is not a prime number'.format(x))
     for x in filter(lambda x: not is_prime(x), numbers_range)]


def is_prime(x: int):
    return not ((x % 2 == 0) | (x % 3 == 0) | (x % 5 == 0) | (x % 7 == 0))


def find_prime(a, b):
    return list(filter(lambda x: is_prime(x), list(range(a, b))))


def opt_find_prime_numbers():
    try:
        variable_a = int(input('Write the first number to start from'))
        while (variable_a < 0):
            variable_a = input('the number {} it\'s not a valid number, please insert a valid number =>'.format(variable_a))
    except Exception as e:
        variable_a = random.randint(10, 65535)
        print('Error {} choosing a random number instead {}'.format(e, variable_a))
    finally:
        print('partenza da ' + str(variable_a))
    try:
        variable_b = int(input('Write the last number to finish'))
        while (int(variable_b) < int(variable_a)):
            variable_a = input('the number {} it\'s not a valid number, please insert a valid number =>'.format(variable_a))
    except Exception as e:
        variable_b = random.randint(int(variable_a) + 1, 65535)
        print('Error {} choosing a random number instead {}'.format(e, variable_a))
    finally:
        print('Finding primes in range({},{})'.format(variable_a, variable_b))
    print_primes(int(variable_a), int(variable_b))


def opt_get_random_prime_number():
    random_number = random.randint(10, 65535)
    print(random.choice(find_prime(1, random_number)))


if __name__ == '__main__':
    is_quit_command = True
    while (is_quit_command):
        command_selected = str(input(
            "\n\nWelcome, choose an option?\n a) print all the prime numbers in a range\n b) "
            "Print a random prime number\n\n => "))
        if command_selected.lower() == 'a':
            opt_find_prime_numbers()
        elif command_selected.lower() == 'b':
            opt_get_random_prime_number()
        elif command_selected.lower() == 'e' or command_selected.lower() == 'esci' or command_selected.lower() == 'exit':
            is_quit_command = not is_quit_command
        else:
            print('Not a valid option')
