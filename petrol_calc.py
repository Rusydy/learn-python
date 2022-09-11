#PETROL CALCULATOR

def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")

#memanggil fungsi untuk dapat  dijalankan
pengenalan_function()

# object data pembeli yang meliputi (nama,nomerHape, pekerjaan) 
data_pembeli = []

# input data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) dari terminal
def identitas_pembeli(nama,nomor_hape,pekerjaan):
    print("Nama Pembeli: ", nama)
    data_pembeli.append(nama)
    print("Nomor Hape: ", nomor_hape)
    data_pembeli.append(nomor_hape)
    print("Pekerjaan: ", pekerjaan)
    data_pembeli.append(pekerjaan)
    return data_pembeli

# get input from terminal
nama = input("Masukkan nama pembeli: ")
nomor_hape = input("Masukkan nomor hape pembeli: ")
pekerjaan = input("Masukkan pekerjaan pembeli: ")

# call function identitas_pembeli
biodata_pembeli = identitas_pembeli(nama,nomor_hape,pekerjaan)

# there are only three types of fuel that can be filled (pertalite, pertamax, and solar)
# pertalite = 10000, pertamax = 12000, solar = 5000

fuels_type_price = {"pertalite": 10000, "pertamax": 12000, "solar": 5000}

# buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pemberli dan jumlah liter kebutuhan
# create a function that identifies the type of car and the amount of fuel needed
car_liter = {"toyota": 10, "honda": 12, "suzuki": 5}

def jenis_mobil (nama_brand,jumlah_liter):
    print("Nama Brand Mobil: ", nama_brand)
    print("Jumlah Liter: ", jumlah_liter)
    return ()

def hitung_biaya_bbm(liter, harga):
    total = liter * harga
    return total

liter = int(input("Masukkan jumlah liter: "))
harga = int(input("Masukkan harga: "))
total_belanja = hitung_biaya_bbm(liter, harga)

print(total_belanja)

# print dengan contoh output yudi telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
# pertamax
print()

# lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
# gunakan recursion


def belanja(uang):
    if (uang >= total_belanja):
        sisa_uang = uang - total_belanja
        belanja(sisa_uang)
        print(sisa_uang)
    else:
        sisa_uang = 0
    return sisa_uang


print("\n\nRecursion Example Results")

uang = int(input("Masukkan jumlah uang: "))
belanja(uang)
# output jika uang 720000 dan total_belanja 360000
# 0
# 360000
