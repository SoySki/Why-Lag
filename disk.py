import psutil
disk = psutil.disk_usage("/")
Total = disk.total / 1024 / 1024 / 1024
print(round(Total, 2,),"GB in total")
Free = disk.free / 1024 / 1024 / 1024
print(round(Free, 2,),"GB free")
