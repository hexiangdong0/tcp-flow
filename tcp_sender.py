import socket
from tcp import PORT, SIZE, FILESIZE
import os

def send(filename):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ''
    port = PORT
    sock.bind((host, port))
    sock.listen(3)
    size = SIZE
    while True:
        conn, addr = sock.accept()
        with open(filename, "rb") as f:
            bytes_to_send = f.read(size)
            conn.send(bytes_to_send)
            while len(bytes_to_send) > 0:
                bytes_to_send = f.read(size)
                conn.send(bytes_to_send)
        conn.close()

def diff_filesize(filename, targ_size):
    if not os.path.exists(filename):
        return targ_size
    return abs(os.path.getsize(filename) / (2 ** 20) - targ_size)

if __name__ == "__main__":
    if diff_filesize("tcp_file", FILESIZE) >= FILESIZE / 10.0:
        os.system(f"dd if=/dev/zero of=tcp_file bs=1M count={FILESIZE}") # generate a file
    send("tcp_file")
