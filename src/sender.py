import utils


class Sender:
    e = 0,
    n = 0,

    def initialize_public_key(self, e, n):
        self.e = e
        self.n = n

    def encryption(self, plaintext):
        splited_message = utils.split_message(plaintext)

        integer_message = utils.convert_to_number(splited_message)

        cipher_text = ""
        for i in integer_message:
            c = pow(i, self.e, self.n)
            cipher_text = cipher_text + " "+str(c)
        return cipher_text[1:]
