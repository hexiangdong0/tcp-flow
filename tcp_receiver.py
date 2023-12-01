import socket
from tcp import PORT, SIZE
import sys
import time
import os

# host = None

def start_client(filename, host='10.0.1.1'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = '10.0.1.1'
    port = PORT
    print("receiver 1")
    sock.connect((host, port))
    print("receiver 2")
    size = SIZE
    filename += str(time.time())
    with open(filename, "wb") as f:
        bytes_received = sock.recv(size)
        while bytes_received:
            # print(len(bytes_received))
            f.write(bytes_received)
            bytes_received = sock.recv(size)
    sock.close()
    os.system('rm -rf {}'.format(filename))

if __name__ == "__main__":
    host = sys.argv[1]
    start_client("downloaded_file", host)
