import socket
import time

HOST = "127.0.0.1"
PORT = 5000

logs = [
    "2026-07-10 13:05:10 INFO LOGIN UserID=1001 Login Successful",
    "2026-07-10 13:05:18 INFO STREAM UserID=1001 Channel=StarSportsHD Stream Started",
    "2026-07-10 13:05:22 ERROR DATABASE ChannelID=205 Buffer Timeout",
    "2026-07-10 13:05:30 INFO ADS UserID=1001 Advertisement Loaded",
    "2026-07-10 13:05:40 INFO RECOMMEND UserID=1001 Suggested=MovieChannel"
]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

for log in logs:
    client.sendall((log + "\n").encode())
    print("Sent:", log)
    time.sleep(2)

client.close()