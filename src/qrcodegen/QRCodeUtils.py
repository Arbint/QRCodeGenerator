import qrcode
from PIL import Image, ImageOps
import math

def GenerateQrCode(savePath, url, iconPath=None, borderColor=(255, 255, 255, 255), version=1):
    print(f"saving qrcode of {url} to {savePath}")
    # # Create a QR code object
    qr = qrcode.QRCode(
        version=version,  # 1–40; with fit=True this is the minimum version used
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # controls error correction
        box_size=40,  # size of the box where QR code will be displayed
        border=4,  # border size around the QR code
    )

    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    qrCodeImg = qr.make_image(fill="black", back_color="white").convert("RGB")

    # # Find and attach Icon
    if iconPath:
        qrCodeCenterIcon = Image.open(iconPath).convert("RGBA")
        borderSize = 40
        qrCodeCenterIcon = ImageOps.expand(qrCodeCenterIcon, border=borderSize, fill=borderColor)
        qrWidth, qrHeight = qrCodeImg.size
        iconSize = qrWidth//4
        qrCodeCenterIcon = qrCodeCenterIcon.resize((iconSize, iconSize), Image.Resampling.LANCZOS)
        iconPos = ((qrWidth - iconSize)//2, (qrHeight - iconSize)//2)
        qrCodeImg.paste(qrCodeCenterIcon, iconPos, mask=qrCodeCenterIcon)

    # Save the image file
    qrCodeImg.save(savePath)
