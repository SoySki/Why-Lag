import psutil
disk = psutil.disk_usage("/")

def total():
    disk = psutil.disk_usage("/")
    total = disk.total / 1024 / 1024 / 1024
    print(round(total, 2,),"GB in total")

def free():
    disk = psutil.disk_usage("/")
    free = disk.free / 1024 / 1024 / 1024
    print(round(free, 2,),"GB free")

def used():
    disk = psutil.disk_usage("/")
    used = disk.used / 1024 / 1024 / 1024
    print(round(used, 2), "GB being used")
