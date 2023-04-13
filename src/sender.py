import utils


class Sender:
    e = 0,
    n = 0,

    def initialize_public_key(self, e, n):
        self.e = int(e)
        self.n = int(n)

    def encryption(self, plaintext):
        cipher_text = pow(int(plaintext), self.e, self.n)
        return cipher_text
