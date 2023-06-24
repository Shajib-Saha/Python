from PIL import Image

me = Image.open('imag-1-removebg-preview.png')
bg = Image.open('eiffeltoren.jpg')

bg.paste(me, (400,700), me)
bg.save('shajib.png')

bg.show()