import utils


class Receiver:
    p = 0,
    q = 0,
    n = 0,
    e = 0,
    phi = 0,
    d = 0

    def initialize_public_key(self, p, q, e):
        self.p = int(p)
        self.q = int(q)
        self.e = int(e)
        self.n = self.p * self.q
        self.calulate_private_key()

    def calulate_private_key(self):
        self.phi = (self.p - 1)*(self.q - 1)
        self.d = utils.mod_inverse(self.e, self.phi)

    def decryption(self, ciphertext):
        print("self e ", self.e)
        print("self d ", self.d)
        print("self n ", self.n)
        m = pow(int(ciphertext), self.d, self.n)
        plaintext = utils.convert_to_string(m)

        return plaintext
