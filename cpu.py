import psutil

def cpu_percent():
    return psutil.cpu_percent(interval=1)
    print(cpu_percent(),"% Being used")

def cpu_stats():
    return psutil.cpu_stats
    print(cpu_stats())