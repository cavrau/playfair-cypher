import unidecode

from typing import List
from .view import PlayFairView
from .encryptor import Encryptor
from .decryptor import Decryptor

ALPHABET = 'abcdefghiklmnopqrstuvwxyz'


class PlayFairController():
    def __init__(self):
        self.key_table = None
        self.view = PlayFairView()

    def __create_key_table_from_list(self, chars: List[str]):
        assert len(chars) == 25
        self.key_table = [
            [], [], [], [], []
        ]
        for i, char in enumerate(chars):
            line = i // 5
            self.key_table[line].append(char)

    def create_key_table(self):
        response = False
        while not response:
            keyword = unidecode.unidecode(
                u'{}'.format(self.view.read_keyword())
            ).lower().replace('j', 'i').replace(' ', '')
            letters = list()
            for letter in keyword:
                if letter not in letters:
                    letters.append(letter)
            for letter in ALPHABET:
                if letter not in letters:
                    letters.append(letter)
            self.__create_key_table_from_list(letters)
            response = self.view.show_key_table(self.key_table)

    def encrypt(self):
        word = self.view.encrypt()
        enc = Encryptor(self.key_table)
        self.view.show_result(enc.encrypt(word))

    def decrypt(self):
        word = self.view.decrypt()
        dec = Decryptor(self.key_table)
        self.view.show_result(dec.decrypt(word))
