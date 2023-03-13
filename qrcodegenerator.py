# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "http://lolcat.in/"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the svg file naming "myqr.svg"
url.svg("myqrlolcat.svg", scale = 8)
  
# Create and save the png file naming "myqr.png"
url.png('myqrlolcat.png', scale = 6)