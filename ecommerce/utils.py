import psutil

battery = psutil.sensors_battery()
percent = str(battery.percent)
print(f'your battery is charged {percent}%')
stor = psutil.disk_partitions()
print(stor)
