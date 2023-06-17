import qrcode

#formatting the qrcode

from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=15,
                   border=5
                   )
qr.add_data("https://codeforces.com/profile/babai404")

qr.make(fit=True)

image = qr.make_image(fill_color="red", back_color="yellow")
image.save("Shajib.png")