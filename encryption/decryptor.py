from .base import BasePlayFair


class Decryptor(BasePlayFair):

    def decrypt_in_column(self, dygraph):
        new_dygraph = ''

        for i, _ in enumerate(self.cypher[0]):
            lines = [line[i] for line in self.cypher]
            if dygraph[0] in lines and dygraph[1] in lines:
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[0]:
                        new_dygraph = lines[index - 1]
                        break
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[1]:
                        new_dygraph += lines[index - 1]
                        break
                break

        return new_dygraph

    def decrypt_in_line(self, dygraph):
        new_dygraph = ''
        for lines in self.cypher:
            if dygraph[0] in lines and dygraph[1] in lines:
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[0]:
                        new_dygraph = lines[index - 1]
                        break
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[1]:
                        new_dygraph += lines[index - 1]
                        break
                break

        return new_dygraph

    def decrypt_dygraph_in_cypher(self, dygraph: str):
        assert len(dygraph) == 2
        dygraph = dygraph.upper()

        new_dygraph = self.decrypt_in_column(dygraph)
        new_dygraph = self.decrypt_in_line(dygraph) if new_dygraph == '' else new_dygraph
        new_dygraph = self.find_in_matrix(dygraph) if new_dygraph == '' else new_dygraph

        return new_dygraph

    def decrypt(self, word: str):
        assert len(word) % 2 == 0
        decrypted_word = ''
        for chunk in self.separate_in_dygraphs(word):
            decrypted_word += self.decrypt_dygraph_in_cypher(chunk)
        decrypted_word = decrypted_word.lower()
        x_array = []
        if 'x' in decrypted_word:
            for i, letter in enumerate(decrypted_word):
                if letter == 'x':
                    first = decrypted_word[i-1] if i-1 > 0 else ''
                    last = decrypted_word[i+1] if i+1 < len(decrypted_word) else ''
                    if first == last:
                        x_array.append(i)

        decrypted_word = bytearray(decrypted_word, 'utf-8')

        for x in x_array:
            del decrypted_word[x]

        return str(decrypted_word, 'utf-8')
