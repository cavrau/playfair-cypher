import re
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
        match = re.search(r'([aA-zZ])\1', word)
        if match is not None:
            repeated_str = match.group()
            word = word.replace(repeated_str, f'{repeated_str[0]}x{repeated_str[1]}')
        return word

    def separate_in_dygraphs(self, word: str) -> List[str]:
        return [
            dygraph if len(dygraph) == 2 else f'{dygraph}x' for dygraph in [
                word[i:i+2] for i in range(0, len(word), 2)
            ]
        ]
