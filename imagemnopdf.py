from PIL import Image
from glob import glob
import os

iml = []


files = glob("*.png")
# rgb.save(PDF_FILE, 'PDF', resoultion=100.0)
for f in files:
    print(f)
    print(f[:-4])
    newname = f[:-4] + ".png"
    print(newname)
    os.rename(f, newname)
files = glob("*.png")
print(files)

# rgba = Image.open(PNG_FILE)
# To avoid ValueError: cannot save mode RGBA 

rgba = Image.open(glob("*.png")[0])
rgb = Image.new('RGB', rgba.size, (255, 255, 255))  # white background
rgb.paste(rgba, mask=rgba.split()[3])               # paste using alpha channel as mask
for img in files:
    rgba2 = Image.open(img)
    rgb2 = Image.new('RGB', rgba2.size, (255, 255, 255))  # white background
    rgb2.paste(rgba2, mask=rgba2.split()[3])               # paste using alpha channel as mask
    iml.append(rgb2)
pdf = "ALL.pdf"

rgb.save(pdf, "PDF" ,resolution=100.0, save_all=True, append_images=iml)