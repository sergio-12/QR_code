from turtle import fillcolor
from webbrowser import BackgroundBrowser
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)

qr.add_data("https://www.youtube.com/watch?v=uW0zmBZpoWM")
img = qr.make_image(fill_color='white', back_color='black')
img.save("QRCode.jpg")