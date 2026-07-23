import sys
from collections import defaultdict

input_file = sys.argv[1]
output_file = sys.argv[2]

mode = "w"

if len(sys.argv) == 4 and sys.argv[3] == "append":
    mode = "a"

counts = defaultdict(int)

with open(input_file, "r") as file:
    for line in file:
        word, value = line.strip().split()
        counts[word] += int(value)

with open(output_file, mode) as file:
    for word in sorted(counts.keys()):
        file.write(f"{word} {counts[word]}\n")

print(f"Reducer completed for {input_file}")