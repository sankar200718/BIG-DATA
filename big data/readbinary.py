import pickle

files = [
    "login_logs.bin",
    "stream_logs.bin",
    "database_logs.bin",
    "ads_logs.bin",
    "recommend_logs.bin"
]

for filename in files:

    print("\n==========", filename, "==========")

    try:

        with open(filename, "rb") as file:

            while True:

                try:
                    log = pickle.load(file)
                    print(log)

                except EOFError:
                    break

    except FileNotFoundError:

        print("File not found.")