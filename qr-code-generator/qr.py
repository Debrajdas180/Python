import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=8,
)
qr.add_data("https://www.isro.gov.in/")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("isro.png")
