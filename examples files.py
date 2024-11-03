import wmi
c= wmi.WMI()
for os in c.Win32_OperatingSystem():
    print(f"OS Name:{os.Name}")
    print(f"Version:{os.Version}")
    print(f"Manufacturer:{os.Manufacturer}")
    print(f"Architecture:{os.OSArchitecture}")




import wmi

c = wmi.WMI()

for adapter in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
    print(f"Adapter:{adapter.Description}")
    print(f"IP Address:{adapter.IPAddress[0]}")
    print(f"MAC Address:{adapter.MACAddress}")

import wmi
c = wmi.WMI()
for process in c.Win32_Process():
    print(f"Process ID: { process.ProcessId}, \ Name:{process.Name}")

import wmi
c = wmi.WMI()
for cpu in c.Win32_Processor():
    print(f"CPU Load:{ cpu.LoadPercentage}%")

import wmi
c = wmi.WMI()
for disk in c.Win32_logicalDisk(DriveType=3):
    print(f" Drive: {disk.DeviceID}, Free Space: {int(disk.FreeSpace)/1e9:.2f} GB, \ Total Size:{int(disk.Size)/1e9:.2f} GB")

