from PIL import Image

def cek_rgb():
    # Input Gambar yang ingin di cek
    image = input("Input Image dengan Extensinya: ")
    citra = Image.open(image)

    # titik koordinat yang ingin di cek
    x = int(input("Input koordinat x: "))
    y = int(input("Input koordinat y: "))

    # Mengambil warna RGB berdasarkan koordinat yang dipilih
    pixel = citra.getpixel((x, y))
    r, g, b = pixel

    # Output RGB dari titik koordinat yang dipilih
    print(f"Warna RGB Image {image} di titik ({x}, {y}): R={r}, G={g}, B={b}")


def ubah_rgb():
    # Input Gambar yang ingin di dirubah
    image = input("Input Image dengan Extensinya: ")
    citra = Image.open(image)

    x = int(input("Masukkan koordinat x: "))
    y = int(input("Masukkan koordinat y: "))

    # Mengambil warna RGB berdasarkan koordinat yang dipilih
    pixel = citra.getpixel((x, y))
    r, g, b = pixel

    print(f"Warna RGB Image {image} di titik ({x}, {y}): R={r}, G={g}, B={b}")

    # memasukkan warna RGB baru dalam format "R G B" pada titik yang dipilih
    input_warna_baru = input(
        "Masukkan warna RGB baru (misalnya, 255 0 0 untuk merah): ")

    # Memecah input RGB baru menjadi tiga komponen warna (R, G, B)
    komponen_warna = input_warna_baru.split()

    # Memastikan ada tiga komponen RGB yang valid
    if len(komponen_warna) == 3:
        r_new, g_new, b_new = map(int, komponen_warna)

        # Ganti warna di titik yang sama dengan warna baru
        warna_baru = (r_new, g_new, b_new)
        citra.putpixel((x, y), warna_baru)

        # Simpan citra yang telah dimodifikasi
        citra.save('C:\Users\Regulust\Documents\Coding\Steganografi\Tugas\Tugas-2\output.bmp')
    else:
        print("Format warna RGB tidak valid. Harap masukkan tiga komponen Warna (R G B).")


while True:
    print("PROGRAM RGB")
    print("-------------")
    print("1. Cek RGB")
    print("2. Ubah RGB")
    print("3. Keluar")

    pilihan = input("Input pilihan: ")

    if pilihan == '1':
        cek_rgb()
    elif pilihan == '2':
        ubah_rgb()
    elif pilihan == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")
