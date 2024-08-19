import qrcode

qr = qrcode.QRCode(version =1, box_size=5, border =5)

qr.add_data('https://youtu.be/YE8PTMSFMUg?si=C235Vw-HaP_nG6Z8') 
qr.make(fit=True) 

img = qr.make_image(fill_color=(255,255,204), back_color=(0,102,102))
img.save('fun_qr.png')