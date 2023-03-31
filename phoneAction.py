from ppadb.client import Client as AdbClient
from datetime import datetime

import subprocess
import time

def adbWakeUp():
    subprocess.check_output(['adb', 'devices'])

    # waiting adb wakeup time
    time.sleep(10)

def getDevice(serial=None):
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)

    # connect list of devices
    devices = client.devices()
    
    # get current device
    if serial != None:
        for tempDevice in devices:
            if tempDevice.serial == serial:
                device = tempDevice
                break
        return device
    # if no serial get first device
    else:
        if devices:
            device = devices[0]
        return 

# @TODO 確認下載本地path & 要如何命名下載圖片(maybe+datetime)
def deviceScreenshot(device, path):
    screenShot = device.screencap()
     

if __name__ == '__main__':
    # serial 'f130295' 裝置序號
    serial = "f130295"
    adbWakeUp()
    getDevice(serial=serial)