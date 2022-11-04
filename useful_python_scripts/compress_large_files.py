"""
This automation script uses the built-in Zip file module that helps you to make your large files smaller by compressing their sizes. Below you can find the script that can compress multiple files in a single zip file.

Compress multiple Files
Can be used for Decompressing files
Much more
"""

# Compress Large Files
import zipfile as Zip


def compressor(files):
    file_zip = Zip.ZipFile("output.zip", "w", Zip.ZIP_DEFLATED)
    for f in files:
        file_zip.write(f, compress_type=Zip.ZIP_DEFLATED)
    file_zip.close()
    print("Compressed")


compressor(["video.mkv", "image.jpg"])
