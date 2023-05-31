import subprocess

def overclock_gpu():
    # Set the desired overclocking parameters
    core_clock = 2000
    memory_clock = 4000
    voltage = 1.5

    # Execute the MSI Afterburner command to apply the overclocking settings
    command = f'msiafterburner.exe /cl -core:{core_clock} -memory:{memory_clock} -voltage:{voltage}'
    subprocess.run(command, shell=True)

# Warning: Overclocking a GPU can cause instability, overheating, and potentially damage your hardware. Use it at your own risk.
