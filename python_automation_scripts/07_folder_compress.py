import zipfile
import os

zipf = zipfile.ZipFile('backup.zip', 'w')
for folder, _, files in os.walk('myfolder'):
    for file in files:
        path = os.path.join(folder, file)
        zipf.write(path)
zipf.close()
print("Backup created.")