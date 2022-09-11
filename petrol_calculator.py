#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 07:39:10 2022

@author: yulizarw
"""

#PETROL CALCULATOR

def pengenalan_function() :
    print ("Selamat datang di SPBU UPNVJ FT")

#memanggil fungsi untuk dapat  dijalankan
pengenalan_function()

# object data pembeli yang meliputi (nama,nomerHape, pekerjaan) 
data_pembeli = []

#masukkan data nama pembeli yang meliputi (nama,nomerHape, pekerjaan) 
def identitas_pembeli(nama,nomor_hape,pekerjaan):
    print("Nama Pembeli: ", nama)
    data_pembeli.append(nama)
    print("Nomor Hape: ", nomor_hape)
    data_pembeli.append(nomor_hape)
    print("Pekerjaan: ", pekerjaan)
    data_pembeli.append(pekerjaan)
    # input data pembeli yang akan diisi oleh user ke list data_pembeli
    return data_pembeli

# biodata_pembeli = identitas_pembeli()
biodata_pembeli = data_pembeli
print(biodata_pembeli)

#Diketahui terdapat jenis bahan bakar yang dapat diisi (pertalait, pertameks, dan selar)
def jenis_bbm(bbm):
    for x, in bbm:
        print(x),

#masukkan data bbm
tipe_bbm =[]

#harga untuk pertalait = 10000, pertamek = 12000, selar = 5000
pertalait = 10000
pertameks = 12000
selar = 5000

# buatlah sebuah  fungsi yang mengidentifikasi jenis mobil pemberli dan jumlah liter kebutuhan
# need more information
def jenis_mobil (nama_brand,jumlah_liter):
    print("Nama Brand Mobil: ", nama_brand)
    print("Jumlah Liter: ", jumlah_liter)
    return ()

#panggil fyungsi jenis_mobil
identifikasi_kendaraan = jenis_mobil()

def hitung_biaya_bbm(liter, harga):
    total = liter * harga
    return total

#panggil fungsi hitung biaya
total_belanja = hitung_biaya_bbm()

print (total_belanja, "a")

# print dengan contoh output yudi telah membeli tipe bbm selar seharga  12000 dengan total belanja 360000 rupiah
print ()

#lakukan pembelajaan jika pembeli memiliki uang senilai tertentu lalu hitunglah sampai habis uangnya untuk dibelanjakan
#gunakan recursion
def belanja(uang):
  if(uang >= total_belanja):
    sisa_uang = uang - total_belanja
    belanja (sisa_uang)
    print(sisa_uang)
  else:
    sisa_uang = 0
  return sisa_uang

print("\n\nRecursion Example Results")
belanja()
#output jika uang 720000 dan total_belanja 360000
#0
#360000