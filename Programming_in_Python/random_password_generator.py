#!/usr/bin/env python3

from string import ascii_letters as alph, digits as dgt, punctuation as spcl
from random import choice, randrange
from sys import argv


class RndmPswdGen:
    """
    Generates random passwords of a specified or recommended minimum length

    Supported password types:
        - case-sensitive alphanumeric
        - case-sensitive alphanumeric with special characters excluding space
        - case-insensitive alphanumeric
        - case-insensitive alphanumeric with special characters excluding space

    If a password is not alphanumeric no symbols in a subset share adjacency:
        - X>1[g0J4Q-j%c+U|D^u/r<S       (case-sensitive)
        - 2t1-0s$8f5v;9,r*e4@6:         (case-insensitive)
        - !B]6C3b+Q2H0v{1#F\7i9d|5R4    (case-sensitive)

    If a password is alphanumeric symbols in a subset can share adjacency:
        - bt90h76l3p                    (case-insensitive)
        - s0918o6x2ptwh3                (case-insensitive)
        - 3wFyRHdOL40                   (case-sensitive)

    Commands:
        - Specify a custom password length:         -l <password-length>
        - Generate alphanumeric password:           -an
        - Generate case-insensitive password:       -ci

    Example #1:
        - input:
            python3 random_password_generator.py
        - output:
            Generated random password #1:  >U{0v2=y-3T%
            Generated random password #2:  1o7S2s4}5^h0
            Generated random password #3:  1#B5]9$r=7x3

    Example #2:
        - input:
            python3 random_password_generator.py -1 20
        - output:
            Generated random password #1:  2u|0x!7-s;1z*9H5~8P>
            Generated random password #2:  7q5<8G+1/P]6N3)h4t0|
            Generated random password #3:  9/Q+5;p%X6<d-8t7y!0B

    Example #3:
        - input:
            python3 random_password_generator.py -1 15 -an
        - output:
            Generated random password #1:  6459Bj3s7JZIO0l
            Generated random password #2:  v0U3w4657y82Zd1
            Generated random password #3:  194ZI5837062fPG

    Example #4:
        - input:
            python3 random_password_generator.py -1 8 -ci
        - output:
            Generated random password #1:  #0a1<7e&
            Generated random password #2:  e3]q7m0/
            Generated random password #3:  p8w5}6;o

    Example #5:
        - input:
            python3 random_password_generator.py -l 10 -an -ci
        - output:
            Generated random password #1:  76y90253ji
            Generated random password #2:  lso7d296bq
            Generated random password #3:  56872eaq01

    Example #6:
        - input:
            python3 random_password_generator.py -an -ci
        - output:
            Generated random password #1:  vx0mj3c5k79z
            Generated random password #2:  415s09vc832m
            Generated random password #3:  novxl5pr349m

    Brute-force attempts required to crack random passwords at length 12 when:
        - case-insensitive alphanumeric (36 symbols):
                - over 300 million attempts, or half on average
        - case-sensitive alphanumeric and punctuation combined (95 symbols):
                - over 6 billion attempts, or half on average

    To calculate brute-force attempts: password length * log2(symbol count)

    Author: Adam Ross
    Date: 01/10/2021
    """

    PW_LEN = 12  # a typically recommended minimum password length

    def __init__(self, pw_len=PW_LEN, is_spcl=True, is_case_snstv=True):
        """
        Random password generator class constructor
        :param pw_len: the password length either specified by user or default
        :param is_spcl: boolean for if password has special characters or not
        :param is_case_snstv: boolean for if password is case-sensitive or not
        """
        assert isinstance(pw_len, int)
        assert isinstance(is_spcl, bool), isinstance(is_case_snstv, bool)
        self.is_case_snstv = is_case_snstv
        self.is_spcl = is_spcl

        # set user specified password len or max if positive, otherwise default
        max_len = (66 if is_case_snstv else 52) if is_spcl else 2 * len(dgt)
        self.pw_len = min(pw_len, max_len) if pw_len > 0 else self.PW_LEN

        self.symbols = dict()  # init symbol subsets dict
        self.i = 0  # init dict key pointer

    def __set_symbol_dict(self):
        """
        Sets a dictionary of alphabet, digital and special char symbol subsets
        :return: dictionary containing subsets of password symbols
        """
        return {0: list(alph) if self.is_case_snstv else list(alph)[:26],
                1: list(dgt),
                2: list(spcl) if self.is_spcl else []}

    def __get_random_symbol(self):
        """
        Gets a random symbol of differing subset to prior symbol in password
        If the password is alphanumeric the sequence of subsets is random
        :return: a random unique symbol
        """
        self.i = choice([subset_i for subset_i in range(len(self.symbols))
                         if (subset_i != self.i or not self.is_spcl)
                         and self.symbols[subset_i]])
        return self.symbols[self.i].pop(randrange(len(self.symbols[self.i])))

    def generate_random_password(self):
        """
        Generates a random password containing unique symbols
        :return: generated random password of a specified length
        """
        self.symbols = self.__set_symbol_dict()  # set new symbol subset dict
        self.i = randrange(len(self.symbols))  # set new dict key pointer
        return "".join(self.__get_random_symbol() for _ in range(self.pw_len))


def process_args(args):
    """
    Pass command line arguments as arguments for new RndmPswdGen instance
    :param args: command line arguments: -an, -ci, -l <password-length>
    :return: instance of RndmPswdGen class
    """
    has_special_chars = False if '-an' in args else True
    is_case_sensitive = False if '-ci' in args else True

    if '-l' in args:
        return RndmPswdGen(pw_len=int(args[args.index('-l') + 1]),
                           is_spcl=has_special_chars,
                           is_case_snstv=is_case_sensitive)
    return RndmPswdGen(is_spcl=has_special_chars,
                       is_case_snstv=is_case_sensitive)


if __name__ == "__main__":
    app = process_args(argv)
    print("Generated random password #1: ", app.generate_random_password())
    print("Generated random password #2: ", app.generate_random_password())
    print("Generated random password #3: ", app.generate_random_password())
