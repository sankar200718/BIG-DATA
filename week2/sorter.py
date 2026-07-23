import sys
import os

partition_file = sys.argv[1]

with open(partition_file, "r") as file:
    lines = file.readlines()

lines.sort()

folder = os.path.dirname(partition_file)
filename = os.path.basename(partition_file)

output_file = os.path.join(folder, "sorted_" + filename)

with open(output_file, "w") as file:
    file.writelines(lines)

print(f"Sorted file created: {output_file}")