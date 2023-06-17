import qrcode as qr

image = qr.make("https://www.facebook.com/shajibsaha.rhidoy")

image.save("Shajib_Saha.png")