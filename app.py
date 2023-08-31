from myclass import IpCounter


try:
    ipcounter = IpCounter('access.log.2017-10-13', False)
    for info in ipcounter:
        print(info)
except Exception as e: 
    print(e)