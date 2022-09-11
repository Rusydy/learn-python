# PETROL CALCULATOR

def pengenalan_function():
    print("Selamat datang di SPBU UPNVJ FT")

# memanggil fungsi untuk dapat  dijalankan
pengenalan_function()

# object data pembeli yang meliputi (nama,nomerHape, pekerjaan)
data_pembeli = []

# input data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) dari terminal

def identitas_pembeli(nama, nomor_hape, pekerjaan):
    print("Nama Pembeli: ", nama)
    data_pembeli.append(nama)
    print("Nomor Hape: ", nomor_hape)
    data_pembeli.append(nomor_hape)
    print("Pekerjaan: ", pekerjaan)
    data_pembeli.append(pekerjaan)
    return data_pembeli

# get input from terminal
nama = input("Masukkan nama pembeli: ")
data_pembeli.append(nama)
nomor_hape = input("Masukkan nomor hape pembeli: ")
data_pembeli.append(nomor_hape)
pekerjaan = input("Masukkan pekerjaan pembeli: ")
data_pembeli.append(pekerjaan)

fuels_type_price = {"pertalite": 10000, "pertamax": 12000, "solar": 5000}

car_type_liter = {"toyota": 10, "honda": 12, "suzuki": 5}


def hitung_biaya_bbm (jumlah_liter, jenis_bbm):
    fuel_price = fuels_type_price[jenis_bbm]
    total_belanja = jumlah_liter * fuel_price
    print("Total Belanja: ", total_belanja)
    return total_belanja

# get input from terminal
jumlah_liter = int(input("Masukkan jumlah liter: "))
jenis_bbm = input("Masukkan jenis bbm: ")

# print jenis 
# call function total_belanja
total_belanja = hitung_biaya_bbm(jumlah_liter, jenis_bbm)

print(data_pembeli[0], "telah membeli tipe bbm", jenis_bbm, "seharga", fuels_type_price[jenis_bbm], "dengan total belanja", total_belanja, "rupiah")

def belanja(uang):
    if uang >= total_belanja:
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
