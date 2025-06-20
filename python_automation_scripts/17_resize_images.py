from PIL import Image
import os

os.makedirs('resized', exist_ok=True)
for file in os.listdir('images'):
    if file.endswith('.jpg'):
        img = Image.open(f'images/{file}')
        img = img.resize((300, 300))
        img.save(f'resized/{file}')
        print(f"Resized {file}")