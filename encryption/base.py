import unidecode
from typing import List
Cypher = List[List[str]]


class BasePlayFair:
    def __init__(self, cypher: Cypher):
        self.cypher = cypher

    def find_in_matrix(self, dygraph):
        for i, lines in enumerate(self.cypher):
            for j, letter in enumerate(lines):
                if dygraph[0] == letter:
                    coords_1 = [i, j]
                elif dygraph[1] == letter:
                    coords_2 = [i, j]
        return f'{self.cypher[coords_1[0]][coords_2[1]]}{self.cypher[coords_2[0]][coords_1[1]]}'

    def normalize_string(self, word: str) -> str:
        word = unidecode.unidecode(u'{}'.format(word)).lower().replace('j', 'i')
        while True:
            old_word = word
            for i in range(0, len(word), 2):
                if i + 1 < len(word) and word[i] == word[i + 1]:
                    word = word.replace(word[i] + word[i + 1], f'{word[i]}x{word[i + 1]}')
                    break
            if old_word == word:
                break
        return word

    def separate_in_dygraphs(self, word: str) -> List[str]:
        return [
            dygraph if len(dygraph) == 2 else f'{dygraph}x' for dygraph in [
                word[i:i+2] for i in range(0, len(word), 2)
            ]
        ]
