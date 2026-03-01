
import os

path = input("Enter directory path: ")

if not os.path.exists(path):
    print("Path does not exist.")
else:
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    print("Total size (MB):", round(total_size / (1024 * 1024), 2))
