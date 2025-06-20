import qrcode

data = "https://yourwebsite.com"
img = qrcode.make(data)
img.save("qrcode.png")
print("QR code generated.")