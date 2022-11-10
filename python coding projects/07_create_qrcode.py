import pyqrcode
# import png 
from pyqrcode import QRCode

a  = "https://instagram.com/suray_vansi_07/"
url = pyqrcode.create(a) #create ka main work qrcode create karna hai
url.svg("myQR.svg",scale = 8)  #svg ek formate hai jisme qrcode generate hota hai
# url.png(myQR.png,scale = 6)