
import qrcode
import os

# Input text to encode
data = input("Enter the text or URL to encode in QR: ")

# Create QR code
qr = qrcode.make(data)

# Save it
folder = "qrcodes"
os.makedirs(folder, exist_ok=True)
filename = os.path.join(folder, "qr_code.png")
qr.save(filename)

print(f"QR Code saved at {filename}")
