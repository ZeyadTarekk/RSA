import utils


class Sender:
    e = 0,
    n = 0,

    def initialize_public_key(self, e, n):
        self.e = int(e)
        self.n = int(n)

    def encryption(self, plaintext):
        print("self e ", self.e)
        # print("self d ", self.d)
        print("self n ", self.n)
        cipher_text = pow(int(plaintext), self.e, self.n)
        return cipher_text
