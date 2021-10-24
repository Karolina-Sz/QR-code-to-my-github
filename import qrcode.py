import qrcode


data = 'https://github.com/Karolina-Sz?tab=repositories'


qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image()

img.save('/Users/karola/Desktop/projekty/githubqrcode.png')