import socket
import sender
import receiver
import utils

sender_client = sender.Sender()
receiver_client = receiver.Receiver()


def reciever_function():
    """
    This function sets up a socket connection to a server, initializes the sender and receiver public keys using the key generation functions in the utils module, and then loops to receive encrypted messages from the server, decrypts them using the receiver's private key, and sends a confirmation message back to the server. The loop continues until the connection is closed.
    """
    host = socket.gethostname()
    port = 5000
    server = socket.socket()
    server.connect((host, port))

    utils.sending_setup(sender_client, server)

    utils.receiving_setup(receiver_client, server)

    while True:
        utils.receive_message(receiver_client, server)

        utils.send_message(sender_client, server)

    connection.close()


reciever_function()
