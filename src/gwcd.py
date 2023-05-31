import subprocess
import json

def get_connected_devices():
    # Execute the command to get connected devices
    command = 'arp -a'
    output = subprocess.check_output(command, shell=True).decode('utf-8')

    # Parse the output and extract relevant information
    devices = []
    lines = output.splitlines()
    for line in lines:
        if 'dynamic' in line.lower() and '-' in line:
            ip, _, mac, _ = line.split()
            devices.append({'ip': ip, 'mac': mac})

    # Return the devices in JSON format
    return json.dumps(devices, indent=4)

# Example usage
connected_devices = get_connected_devices()
print(connected_devices)
