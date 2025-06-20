import psutil

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory.percent}%")
print(f"Disk Usage: {disk.percent}%")