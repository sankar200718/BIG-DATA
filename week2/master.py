import os
import subprocess

# Create required folders
os.makedirs("chunks", exist_ok=True)
os.makedirs("partitions", exist_ok=True)
os.makedirs("output", exist_ok=True)

for generated_file in [
    "partitions/partition0.txt",
    "partitions/partition1.txt",
    "partitions/sorted_partition0.txt",
    "partitions/sorted_partition1.txt",
    "output/result.txt",
]:
    if os.path.exists(generated_file):
        os.remove(generated_file)

print("====================================")
print("      MAPREDUCE ENGINE STARTED")
print("====================================")

# Step 1: Split the input file
print("\n[1] Splitting Input File...")
subprocess.run(["python", "spliter.py"])

# Step 2: Run Mapper on Chunk 1
print("\n[2] Running Mapper on Chunk 1...")
subprocess.run(["python", "mapper.py", "chunks/chunk1.txt", "mapper1_output.txt"])

# Step 3: Run Mapper on Chunk 2
print("\n[3] Running Mapper on Chunk 2...")
subprocess.run(["python", "mapper.py", "chunks/chunk2.txt", "mapper2_output.txt"])

# Step 4: Partition Mapper Outputs
print("\n[4] Partitioning Intermediate Data...")
subprocess.run(["python", "partitioner.py", "mapper1_output.txt"])
subprocess.run(["python", "partitioner.py", "mapper2_output.txt"])

# Step 5: Sort Partition Files
print("\n[5] Sorting Partition Files...")
subprocess.run(["python", "sorter.py", "partitions/partition0.txt"])
subprocess.run(["python", "sorter.py", "partitions/partition1.txt"])

# Step 6: Run Reducers
print("\n[6] Running Reducers...")
subprocess.run([
    "python",
    "reducer.py",
    "partitions/sorted_partition0.txt",
    "output/result.txt"
])

subprocess.run([
    "python",
    "reducer.py",
    "partitions/sorted_partition1.txt",
    "output/result.txt",
    "append"
])

print("\n====================================")
print(" MAPREDUCE EXECUTION COMPLETED")
print("====================================")
print("Final Output : output/result.txt")