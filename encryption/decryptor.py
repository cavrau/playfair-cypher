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

        new_dygraph = self.decrypt_in_column(dygraph)
        new_dygraph = self.decrypt_in_line(dygraph) if new_dygraph == '' else new_dygraph
        new_dygraph = self.find_in_matrix(dygraph) if new_dygraph == '' else new_dygraph

        return new_dygraph

    def decrypt(self, word: str):
        word = word.lower()
        decrypted_word = ''
        for chunk in self.separate_in_dygraphs(word):
            decrypted_word += self.decrypt_dygraph_in_cypher(chunk)
        return decrypted_word.lower()
