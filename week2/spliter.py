import os

INPUT_FILE = "input.txt"
CHUNK_FOLDER = "chunks"

os.makedirs(CHUNK_FOLDER, exist_ok=True)

with open(INPUT_FILE, "r") as file:
    lines = file.readlines()

mid = len(lines) // 2

chunk1 = lines[:mid]
chunk2 = lines[mid:]

with open(os.path.join(CHUNK_FOLDER, "chunk1.txt"), "w") as file:
    file.writelines(chunk1)

with open(os.path.join(CHUNK_FOLDER, "chunk2.txt"), "w") as file:
    file.writelines(chunk2)

print("Input file split successfully.")