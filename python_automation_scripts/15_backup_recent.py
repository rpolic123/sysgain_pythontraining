import os, shutil, time

src = 'project'
dst = 'backup'
now = time.time()
os.makedirs(dst, exist_ok=True)

for root, _, files in os.walk(src):
    for f in files:
        path = os.path.join(root, f)
        if now - os.path.getmtime(path) < 86400:
            shutil.copy2(path, dst)
            print(f"Backed up: {f}")