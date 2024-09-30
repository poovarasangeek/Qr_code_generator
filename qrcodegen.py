import pyqrcode
s="https://github.com/poovarasangeek"
qrcode=pyqrcode.create(s)
qrcode.svg('poovarasangeek.svg',scale=6)

