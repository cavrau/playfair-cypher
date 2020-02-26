from .base import BasePlayFair


class Encryptor(BasePlayFair):

    def encrypt(self, word: str) -> str:
        word = self.normalize_string(word)
        encrypted_word = ''
        for dygraph in self.separate_in_dygraphs(word):
            encrypted_word += self.encrypt_dygraph_in_cypher(dygraph)
        return encrypted_word

    def encrypt_in_column(self, dygraph) -> str:
        new_dygraph = ''

        for i, _ in enumerate(self.cypher[0]):
            lines = [line[i] for line in self.cypher]
            if dygraph[0] in lines and dygraph[1] in lines:
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[0]:
                        new_dygraph = lines[index + 1] if index + 1 < len(lines) else lines[0]
                        break
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[1]:
                        new_dygraph += lines[index + 1] if index + 1 < len(lines) else lines[0]
                        break
                break

        return new_dygraph

    def encrypt_in_line(self, dygraph) -> str:
        new_dygraph = ''
        for lines in self.cypher:
            if dygraph[0] in lines and dygraph[1] in lines:
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[0]:
                        new_dygraph = lines[index + 1] if index + 1 < len(lines) else lines[0]
                        break
                for index, c_letter in enumerate(lines):
                    if c_letter == dygraph[1]:
                        new_dygraph += lines[index + 1] if index + 1 < len(lines) else lines[0]
                        break
                break

        return new_dygraph

    def encrypt_dygraph_in_cypher(self, dygraph: str) -> str:
        assert len(dygraph) == 2

        new_dygraph = self.encrypt_in_column(dygraph)
        new_dygraph = self.encrypt_in_line(dygraph) if new_dygraph == '' else new_dygraph
        new_dygraph = self.find_in_matrix(dygraph) if new_dygraph == '' else new_dygraph

        return new_dygraph
