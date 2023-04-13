import key_generation
import sender as send
import receiver as rec
import utils
import time
import matplotlib.pyplot as plt


sender = send.Sender()
receiver = rec.Receiver()

key_lengths = []
encryption_time = []
decryption_time = []

# with open('efficiency.txt', 'w') as f:
#     for n in range(27, 3000, 1):
#         p, q = utils.generate_pq_bybits(n)
#         f.write(str(p) + "\n")
#         f.write(str(q) + "\n")
#         f.write("\n")
# f.close()

test_file = open("graphs_msg.txt", "r")
lines = test_file.read().splitlines()
message = lines[0]
test_file.close()

test_file = open("efficiency.txt", "r")
lines = test_file.read().splitlines()
i = 0
j = 27
while i < len(lines)-1:
    print(lines[i])
    p = int(lines[i])
    q = int(lines[i+1])
    key_lengths.append(j)
    i += 3
    j += 1
    e = key_generation.generate_e((p-1) * (q-1))

    receiver.p = int(p)
    receiver.q = int(q)
    receiver.e = int(e)
    receiver.n = receiver.p*receiver.q
    receiver.initialize_public_key(int(p), int(q), int(e))
    sender.initialize_public_key(e, p*q)
    time1 = 0
    time2 = 0

    splited_message = utils.split_message(message)
    m, count = utils.convert_to_number(splited_message)
    C = ''
    decryptedMessage = ''
    for ii in m:
        start_time = time.time()
        c = sender.encryption(ii)
        end_time = time.time()
        time1 = time1 + (end_time - start_time)

        start_time = time.time()
        decryptedc = receiver.decryption(c)
        end_time = time.time()
        time2 = time2 + (end_time - start_time)
        decryptedMessage = decryptedMessage + decryptedc

    encryption_time.append(time1)

    decryption_time.append(time2)

test_file.close()
print("time taken:")
print(encryption_time)
print("corresponding key lengths in bits:")
print(key_lengths)

plt.plot(key_lengths, encryption_time)
plt.xlabel('Key length (bits)')
plt.ylabel('encryption time (s)')
plt.title('RSA efficiency')
plt.show()

print("time taken:")
print(decryption_time)
print("corresponding key lengths in bits:")
print(key_lengths)

plt.plot(key_lengths, decryption_time)
plt.xlabel('Key length (bits)')
plt.ylabel('decryption time (s)')
plt.title('RSA efficiency')
plt.show()
