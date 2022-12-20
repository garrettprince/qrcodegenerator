# NOTICE Change data and img.save name before running for unique codes

# Importing library
import qrcode
 
# Data to encode
data = "www.example.com"
 
# Creating an instance of QRCode class
qr = qrcode.QRCode(version = 2,
                   box_size = 10,
                   border = 5)
 
# Adding data to the instance 'qr'
qr.add_data(data)
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'black',
                    back_color = 'white')
 
img.save('example.png')