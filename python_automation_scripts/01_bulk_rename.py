import os

folder = 'test_folder'
prefix = 'img_'
for i, filename in enumerate(os.listdir(folder)):
    if filename.endswith('.jpg'):
        old = os.path.join(folder, filename)
        new = os.path.join(folder, f"{prefix}{i+1}.jpg")
        os.rename(old, new)
        print(f"Renamed: {old} -> {new}")