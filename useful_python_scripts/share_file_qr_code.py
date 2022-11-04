"""
Need to share files with someone in an easier way. Then this automation script will help you to create a QR code of your file that you can share with anyone and when someone scans the Qrcode the file that you share is now downloadable.

* Share Files with anyone
* Use in your project
* Share any file format
* Much more
"""

# Share File QrCode
# pip install share-file-qr
# pip install qrcode
import subprocess as proc
import qrcode


def share_files_qr(file):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )
    qr.add_data(f"http://192.168.0.105:4000/file/{file}")
    qr.make(fit=True)
    qr.make_image().save("qrcode.png")
    proc.call(f"share-file-qr {file}", stderr=proc.STDOUT)


share_files_qr("test.png")