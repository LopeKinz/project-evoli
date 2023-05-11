import platform,socket,re,uuid,json,psutil,logging

def getSystemInfo():
    try:
        info = {'platform': platform.system()}
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram'] = f"{str(round(psutil.virtual_memory().total / 1024.0**3))} GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)


#add webhook funktion
