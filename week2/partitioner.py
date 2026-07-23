import os
import sys
import hashlib

mapper_output = sys.argv[1]

os.makedirs("partitions", exist_ok=True)

partition0 = open("partitions/partition0.txt", "a")
partition1 = open("partitions/partition1.txt", "a")

with open(mapper_output, "r") as file:
    for line in file:
        word, value = line.strip().split()

        partition = int.from_bytes(hashlib.md5(word.encode("utf-8")).digest(), "big") % 2

        if partition == 0:
            partition0.write(f"{word} {value}\n")
        else:
            partition1.write(f"{word} {value}\n")

partition0.close()
partition1.close()

print("Partitioning completed.")