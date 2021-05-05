import psutil
import wmi
from tqdm import tqdm
from time import sleep
def progress(range):
    for i in tqdm(range, desc ="Progress : "):
            sleep(.1)

f = wmi.WMI()
l = []
#To Scan How Much Processing Tasks
for process in f.Win32_Process():
    l.append(process.ProcessId)

# gives an object with many fields
ram1 = psutil.virtual_memory()
print("Scanning Ram : \n")
progress(ram1)
print()
# you can convert that object to a dictionary 
dict(psutil.virtual_memory()._asdict())
# you can have the percentage of used RAM
ram = psutil.virtual_memory().percent
#You Can Have The Available Ram 
avram = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
print(f"Hold On We've Found {len(l)} Running Process !! \n")
print(f"Those Processes Only Left For You "+"{:.1f}".format(avram)+"%"+" available Of Your RAM !!\n")
print(f"The Used ram is : {ram}%\n")
print("We Will Load Your Running Processes Please Wait \n")
progress(l)
print()
print("ID:        Process name:\n")
for process in f.Win32_Process():
    print(f"{process.ProcessId:<10} {process.Name}")

print(f"\nThe Number Of Actively Running Tasks {len(l)} \n")

input()