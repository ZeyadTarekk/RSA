import socket
import sender
import receiver
import utils

sender_client = sender.Sender()
receiver_client = receiver.Receiver()


def sender_function():
    host = socket.gethostname()
    port = 5000
    server = socket.socket()
    server.bind((host, port))
    server.listen(2)
    connection, address = server.accept()

    print("Connection accepted from: "+str(address))

    utils.receiving_setup(receiver_client, connection)

    utils.sending_setup(sender_client, connection)

    while True:
        utils.send_message(sender_client, connection)

        utils.receive_message(receiver_client, connection)

    connection.close()


sender_function()
