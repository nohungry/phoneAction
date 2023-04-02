from ppadb.client import Client as AdbClient
from datetime import datetime

import subprocess
import os
import time

def adbWakeUp():
    subprocess.check_output(['adb', 'devices'])

    # waiting adb wakeup time
    time.sleep(10)

def monitorUp(device):
    device.shell("input keyevent 26")
    time.sleep(3)
    device.shell("input keyevent 82")

def connectDevice(serial=None):
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
        return device

# @TODO 確認下載本地path & 要如何命名下載圖片(maybe+datetime)
def screenshot(device, filename):
    # 獲取當前手機的snapshot
    screenShot = device.screencap()
    # 獲取當前資料夾位置
    currentDir = os.getcwd()
    # 組合成特定名稱的資料夾
    # e.g. DeepSea Folder
    filePath = os.path.join(currentDir, filename)
    # 開始處理時間並添加到到snapshot後面後墜
    nowTime = datetime.today().strftime("%Y%m%d_%H%M")
    temp = os.path.join(filePath, r"screen_" + nowTime + ".png")
    # 開始寫入到本機對應的資料夾
    with open(temp, "wb")as f:
        f.write(screenShot)

    return temp

if __name__ == '__main__':
    # serial 'f130295' 裝置序號
    serial = "f130295"
    adbWakeUp()
    device = connectDevice(serial=serial)
    monitorUp(device)