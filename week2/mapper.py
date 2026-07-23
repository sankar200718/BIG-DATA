import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        word = line.strip()
        if word:
            outfile.write(f"{word} 1\n")

print(f"Mapper completed for {input_file}")