import subprocess

def getDevice(serial=None):
    # get device list
    output = subprocess.check_output(['adb', 'devices'])
    devices = output.decode().strip().split('\n')[1:]

    # multiple device connect, allows the user to select device
    if len(devices) > 1:
        print('Multiple devices connected:')
        for i, device in enumerate(devices):
            print(f'{i+1}. {device}')
        index = int(input('Enter device index: '))
        device_serial = devices[index-1].split('\t')[0]
    elif len(devices) == 1:
        device_serial = devices[0].split('\t')[0]
    else:
        print('No device connected')
        exit()

    # get device message
    output = subprocess.check_output(['adb', '-s', device_serial, 'shell', 'getprop', 'ro.product.model'])
    device_model = output.strip().decode()

    print('Device model:', device_model)

    return device_serial

def getSnapShot():
    screenShot = subprocess.check_output(['adb', 'shell', 'screencap', '-p'])
    with open("screenshot01.png", "wb") as f:
        f.write(screenShot)

if __name__ == '__main__':
    deviceSerial = getDevice()
    getSnapShot()
