import psutil


ram = psutil.virtual_memory()
def ram_total():
    total = ram.total / 1024 / 1024 / 1024
    return(round(total, 2))

def ram_used():
    used = ram.used / 1024 / 1024 / 1024
    return(round(used, 2))

def ram_free():
    free = ram.free / 1024 / 1024 / 1024
    return(round(free, 2))