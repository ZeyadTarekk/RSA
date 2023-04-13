import utils


class Receiver:
    p = 0,
    q = 0,
    n = 0,
    e = 0,
    phi = 0,
    d = 0

    def initialize_public_key(self, p, q):
        self.p = p
        self.q = q

    def calulate_private_key(self):
        self.phi = (self.p - 1)*(self.q - 1)
        self.d = utils.mod_inverse(self.e, self.phi)

    def decryption(self, ciphertext):
        # calulate private key is called

        ciphertext = ciphertext.split(" ")

        plaintext = ""
        for i in ciphertext:
            m = pow(i, self.d, self.n)
            plaintext = plaintext + utils.convert_to_string(m)

        return plaintext
