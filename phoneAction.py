from ppadb.client import Client as AdbClient

def getDevice(serial=None):
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)

    # connect list of devices
    devices = client.devices()
    
    # 