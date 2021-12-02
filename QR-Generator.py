import qrcode

name = input("Enter the data to make a QR code :")
generate_image = qrcode.make(name)
generate_image.save('QR.png')





