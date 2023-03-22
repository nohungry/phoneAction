from ppadb.client import Client as AdbClient

# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)
# print(client.version())

# 列出已連接的設備
devices = client.devices()
print(devices)

# 取得第一個設備的屏幕截圖
if devices:
    device = devices[0]
    image = device.screencap()
    with open('screenshot01.png', 'wb') as f:
        f.write(image)