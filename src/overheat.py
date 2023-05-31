import wmi

def turn_off_all_fans():
    c = wmi.WMI()
    for fan in c.Win32_Fan():
        fan.SetSpeed(0)
