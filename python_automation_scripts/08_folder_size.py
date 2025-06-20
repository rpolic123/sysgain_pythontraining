import os

folder = 'myfolder'
total_size = 0
for dirpath, _, filenames in os.walk(folder):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        total_size += os.path.getsize(fp)
print(f"Total size of '{folder}': {total_size / (1024**2):.2f} MB")