# Import Library
from PIL import Image
import piexif
import os
import time 

# Masukan Pesan yang akan disisipkan
message = input("Input pesan rahasia : ")

# Mengambil directory dari program saat ini dan menggabungkan ke nama file beserta ekstensinya
curr_dir = os.path.dirname(os.path.abspath(__file__))
image = input("Input Image dengan Extensinya: ")
img_path = os.path.join(curr_dir, image)
im = Image.open(img_path, 'r')

# Jika terdapat exif/metadata pada gambar, maka pesan pada exif dihapus kemudian ditimpa dengan pesan yang baru
if "exif" in im.info:
    exif_dict = piexif.load(im.info["exif"])
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = message
    exif_bytes = piexif.dump(exif_dict)
# Jika tidak terdapat exif/metadata pada gambar, maka pesan akan langsung ditimpa pada exif gambar
else:
    exif_bytes = piexif.dump({"0th":{piexif.ImageIFD.ImageDescription:message}})

print("\n\033[92mPESAN RAHASIA BERHASIL DISISIPKAN\033[0m\n")
time.sleep(1)

# Menyimpan gambar baru atau menimpa gambar yang sudah ada, ekstensi file harus sama
new_img_name = input("Masukan nama file baru dengan ekstensi (Ekstensi harus sama dengan input): ")

# Mengambil directory path dari folder saat ini dan menggabungkan dengan nama file besereta ekstensinya
newimg_path = os.path.join(curr_dir, new_img_name)
im.save(newimg_path, str(new_img_name.split(".")[1].upper()), exif=exif_bytes)

print("\033[92mFILE BERHASIL DISIMPAN\033[0m")
time.sleep(2)