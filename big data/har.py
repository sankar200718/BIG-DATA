import socket
import threading
import pickle
import re

HOST = "0.0.0.0"
PORT = 5000

regex = re.compile(
    r"\d{4}-\d{2}-\d{2} "
    r"\d{2}:\d{2}:\d{2} "
    r"(INFO|ERROR|WARNING) "
    r"(LOGIN|STREAM|DATABASE|ADS|RECOMMEND) .+"
)


def save_binary(server_type, data):
    filename = server_type.lower() + "_logs.bin"

    with open(filename, "ab") as file:
        pickle.dump(data, file)


def process_log(log):

    if not regex.match(log):
        print("Invalid Log:", log)
        return

    parts = log.split()

    payload = {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "server": parts[3],
        "message": " ".join(parts[4:])
    }

    print("Received:", payload)

    save_binary(payload["server"], payload)


def handle_client(conn):

    buffer = ""

    while True:

        data = conn.recv(1024)

        if not data:
            break

        buffer += data.decode()

        while "\n" in buffer:

            line, buffer = buffer.split("\n", 1)

            process_log(line)

    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Harvester Running...")

while True:

    conn, addr = server.accept()

    print("Connected:", addr)

    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()