import utils
import key_generation
import sender as send
import receiver as rec
import time
import matplotlib.pyplot as plt
import sympy


def mathematicalAttack(ciphertext, n, e):
    ciphertext = ciphertext.split(" ")
    recovered = ''
    rece = rec.Receiver()

    for p in range(2, int((n**0.5)+1)):
        if n % p == 0:

            rece.initialize_public_key(p, n//p, e)
            break

    rece.e = e
    rece.n = rece.p*rece.q
    rece.key_computed = False
    for c in ciphertext:
        recovered = recovered + rece.decryption(c)

    return recovered


while True:
    time_or_test = input(
        "To test attacks press 1, To test the key length vs attack time press 2: ")
    p = 0
    q = 0
    if time_or_test == "1":

        receiver = rec.Receiver()
        sender = send.Sender()

        p, q = utils.generate_p_q(15)

        print("p : ", p)
        print("q : ", q)

        receiver.p = p
        receiver.q = q
        receiver.n = p*q

        receiver.e = key_generation.generate_e((receiver.p-1) * (receiver.q-1))

        e = receiver.e
        p = receiver.p
        q = receiver.q

        msg = input("Enter message: ")

        sender.initialize_public_key(receiver.e, receiver.p*receiver.q)
        receiver.initialize_public_key(p, q, e)

        splited_message = utils.split_message(msg)

        m, count = utils.convert_to_number(splited_message)
        ciphertext = ''
        plaintext = ''
        for i in m:
            c = sender.encryption(i)
            d = receiver.decryption(c)
            plaintext = plaintext + d
            ciphertext = ciphertext + " " + str(c)
        ciphertext = ciphertext[1:]
        with open('attacks_test.txt', 'w') as f:
            f.write(
                "cipher text, (e, n) that attacker want to attack" + "\n")
            f.write(str(ciphertext) + "\n")
            f.write(str(receiver.e) + "\n")
            f.write(str(receiver.p*receiver.q))
        f.close()

        attacker_data = open('attacks_test.txt', "r")
        lines = attacker_data.read().splitlines()
        i = 1
        while i < len(lines)-1:
            ciphertext = lines[i]
            e = int(lines[i+1])
            n = int(lines[i+2])
            i += 4
        attacker_data.close()

        recovered = mathematicalAttack(ciphertext, n, e)

        with open('attack_results.txt', 'w') as f:
            f.write("Original message: " + msg + "\n")
            f.write("Recovered message: " + recovered + "\n")
            f.close()
        if (plaintext == recovered):
            print("The attack is done, hard luck next time!")

    elif time_or_test == "2":
        test_file = open("graphs_msg.txt", "r")
        lines = test_file.read().splitlines()
        msg = lines[0]
        test_file.close()

        # put them in text file to use later
        # with open('time_attack.txt', 'w') as f:
        #     for n in range(1, 65, 2):
        #         p, q = utils.generate_pq_bybits(n)
        #         f.write(str(p) + "\n")
        #         f.write(str(q) + "\n")
        #         f.write("\n")
        # f.close()

        key_lengths = []
        time_to_attack = []
        sender = send.Sender()
        receiver = rec.Receiver()

        Bob_data = open("time_attack.txt", "r")
        lines = Bob_data.read().splitlines()
        i = 0
        j = 1

        C_list = []
        e_list = []
        n_list = []

        while i < len(lines)-2:
            receiver.p = int(lines[i])
            receiver.q = int(lines[i+1])

            receiver.e = key_generation.generate_e(
                (receiver.p-1) * (receiver.q-1))

            sender.initialize_public_key(receiver.e, receiver.p*receiver.q)

            splited_message = utils.split_message(msg)
            m, count = utils.convert_to_number(splited_message)

            ciphertext = ''
            for ii in m:
                c = sender.encryption(ii)
                ciphertext = ciphertext + " " + str(c)
            ciphertext = ciphertext[1:]

            key_lengths.append(j)

            start_time = time.time()
            recovered = mathematicalAttack(
                ciphertext, receiver.p*receiver.q, receiver.e)
            end_time = time.time()
            print('number of bits = ', j, '- Take time = ', end_time - start_time)

            time_to_attack.append(end_time - start_time)

            C_list.append(ciphertext)
            e_list.append(receiver.e)
            n_list.append(receiver.p*receiver.q)
            j += 2
            i += 3

        Bob_data.close()

        with open('attacker_data.txt', 'w') as f:
            for k in range(len(C_list)):
                f.write(str(C_list[k]) + "\n")
                f.write(str(e_list[k]) + "\n")
                f.write(str(n_list[k])+"\n")
                f.write("\n")
        f.close()

        fig, ax = plt.subplots()
        ax.plot(key_lengths, time_to_attack, linewidth=2.0)
        ax.set_title("Key length(bits) vs Time to attack")
        ax.set_xlabel("Key length(bits)")
        ax.set_ylabel("Time to attack (s)")
        plt.show()

    else:
        print("Please choose 1, 2 ")
