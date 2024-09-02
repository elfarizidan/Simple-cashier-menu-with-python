#Muhammad Zidan Alfarizi
#102042300196
#S1SI-23-01

#NB : Ketika memilih pembayaran menggunakan debit, pin debit dan saldo bisa dilihat di line 15


daftar_barang = {
    "pulpen": 5000,
    "buku": 3000,
    "pensil": 4000,
    "penghapus": 2000
}

daftar_kartu_debit = {
    121212 : 1000000, 
    323232 : 400000,
    101010 : 120000,
    555555 : 80000,
}

isi_keranjang = {}

def masuk_barang_ke_keranjang():
    for key, value in daftar_barang.items() :
        print(f"{key} Rp.{value:,.2f}")
    nama_barang = input("\nMasukkan Nama Barang : ").lower()
    jumlah_beli = int(input("Masukkan jumlah barang yang ingin dibeli : "))
    if nama_barang in daftar_barang:
        harga_barang = daftar_barang[nama_barang]
        total_harga = harga_barang * jumlah_beli
        if nama_barang in isi_keranjang:
            isi_keranjang[nama_barang] += jumlah_beli 
        else:
            isi_keranjang[nama_barang] = jumlah_beli
        print("Barang berhasil dimasukkan ke keranjang.")
    else:
        print("Barang tidak ada")     

def hapus_barang_dari_keranjang():
    if isi_keranjang:
        nama_barang = input("Masukkan Nama Barang yang ingin dihapus dari keranjang: ").lower()
        if nama_barang in isi_keranjang:
            del isi_keranjang[nama_barang]
            print("Barang berhasil dihapus dari keranjang")
        else:
            print("Barang tidak ditemukan dalam keranjang")
    else:
        print("Keranjang kosong!") 

def ganti_nama_barang():
    if isi_keranjang:
        nama_ganti = input("Masukkan Nama Barang yang ingin diganti : ").lower()
        if nama_ganti in isi_keranjang:
            harga_barang = isi_keranjang.pop(nama_ganti)
            nama_baru = input("Masukkan Nama Barang baru : ").lower()
            isi_keranjang[nama_baru] = harga_barang
            print("Nama Barang berhasil diganti")
        else:
            print("Barang tidak ditemukan!")
    else:
        print("Keranjang kosong!")

def tampil_isi_keranjang():
    if isi_keranjang:
        print("Isi Keranjang :")
        total_isi_keranjang = 0
        for barang_keranjang, jumlah_barang in isi_keranjang.items():
            harga_barang = daftar_barang[barang_keranjang]
            total_harga = harga_barang * jumlah_barang
            total_isi_keranjang += total_harga
            print(f"{barang_keranjang} Jumlah: {jumlah_barang} Total harga : Rp.{total_harga}")
        print(f"Total isi keranjang : Rp.{total_isi_keranjang}")
    else:
        print("Keranjang kosong!")

def bayar_tunai() :
    print("Anda memilih membayar menggunakan tunai")

    if isi_keranjang:
        print("\nIsi Keranjang :\n")
        total_isi_keranjang = 0
        for barang_keranjang, jumlah_barang in isi_keranjang.items():
            harga_barang = daftar_barang[barang_keranjang]
            total_harga = harga_barang * jumlah_barang
            total_isi_keranjang += total_harga

            if total_harga >= 50000 :
                harga_diskon = total_isi_keranjang * 0.3
                total_isi_keranjang -= harga_diskon
                print("\nSelamat anda mendapatkan diskon 30%\n")

            pajak = total_isi_keranjang * 0.1
            harga_fix = total_isi_keranjang + pajak
            print(f"\n{barang_keranjang} Jumlah: {jumlah_barang} Total harga : Rp.{total_harga:,.2f}")
        print(f"Total isi keranjang setelah diskon : Rp.{total_isi_keranjang:,.2f}")
        print(f"Pajak 10%                          : Rp.{pajak:,.2f}")
        print(f"Harga yang harus anda bayar        : Rp.{harga_fix:,.2f}")


    masuk_nominal = int(input("Masukkan nominal uang : "))

    if masuk_nominal < harga_fix :
        print("Uang anda kurang! ketik '0' untuk kembali ke menu utama")
        return bayar_tunai()
    
    if masuk_nominal == 0 :
        return main()
    
    else :
        kembalian = masuk_nominal - harga_fix
        print(
            f"""
===INVOICE===
{barang_keranjang} Jumlah: {jumlah_barang} Total harga : Rp.{total_harga:,.2f}
Total harga barang : Rp.{total_isi_keranjang:,.2f}
Pajak              : Rp.{pajak:,.2f}
Harga total        : Rp.{harga_fix:,.2f}
Uang cash          : Rp.{masuk_nominal:,.2f}
Kembalian          : Rp.{kembalian:,.2f}"""
        )
    isi_keranjang.clear()

def debit() :
    print("Anda memilih membayar menggunakan debit")

    if isi_keranjang:
        print("Isi Keranjang :")
        total_isi_keranjang = 0
        for barang_keranjang, jumlah_barang in isi_keranjang.items():
            harga_barang = daftar_barang[barang_keranjang]
            total_harga = harga_barang * jumlah_barang
            total_isi_keranjang += total_harga

            if total_harga >= 50000 :
                harga_diskon = total_isi_keranjang * 0.3
                total_isi_keranjang -= harga_diskon
                print("\nSelamat anda mendapatkan diskon 30%\n")

            pajak = total_isi_keranjang * 0.1
            harga_fix = total_isi_keranjang + pajak
            print(f"{barang_keranjang} Jumlah: {jumlah_barang} Total harga : Rp.{total_harga:,.2f}")
        print(f"Total isi keranjang setelah diskon: Rp.{total_isi_keranjang:,.2f}")
        print(f"Pajak 10%                         : Rp.{pajak:,.2f}")
        print(f"Harga yang harus anda bayar       : Rp.{harga_fix:,.2f}")

    else :
        print("Keranjang kosong!")
        return main()

    try :
        masuk_pin = int(input("Masukkan PIN anda : "))
        for pin, saldo in daftar_kartu_debit.items() :
            if masuk_pin in daftar_kartu_debit :
                saldo = daftar_kartu_debit[masuk_pin]
                if saldo < harga_fix :
                    print("\nSaldo anda kurang\n")
                    return debit()
                
                else :
                    sisa_saldo = saldo - harga_fix
                    print(
            f"""\n
===INVOICE===
{barang_keranjang} Rp.{total_harga:,.2f}
Total setelah diskon     : Rp.{total_isi_keranjang:,.2f}
Harga pajak              : Rp.{pajak:,.2f}
Harga yang harus dibayar : Rp.{harga_fix:,.2f}
Metode bayar             : DEBIT
Sisa saldo               : Rp.{sisa_saldo:,.2f}\n""")

            else :
                print("Pin debit tidak ditemukan!")
                return debit()
    except ValueError :
        print("Print barupa angka!")
        return debit()
    
    isi_keranjang.clear()
    return main()

def admin() :
    while True :
        print(
            """
1. Ganti harga barang
2. Tambah barang
3. Hapus barang
4. Tampilkan barang dan harga
5. Kembali ke menu utama"""
        )

        pilih_admin = int(input("Masukkan pilihan : "))

        if pilih_admin == 1 : 
            try :
                ganti_nama = input("Masukkan nama yang mau diganti harganya : ")
                ganti_harga = int(input("Masukkan harga : "))

                daftar_barang.update({ganti_nama : ganti_harga})

            except ValueError :
                return admin()
            
        elif pilih_admin == 2 :
            try :
                nambah_barang = input("Masukkan nama barang : ")
                harga_barang = int(input("Masukkan harga barang : "))

                if nambah_barang in daftar_barang.items() :
                    print("Barang sudah ada di list")
                    return admin
                
                daftar_barang [nambah_barang] = harga_barang

            except ValueError :
                print()
                return admin()
            
        elif pilih_admin == 3 :
            pilih_barang = input("Pilih barang yang mau dihapus : ")
            del daftar_barang[pilih_barang]

        elif pilih_admin == 4 :
            for barang, harga in daftar_barang.items() :
                print(f"{barang} : Rp.{harga}")

        elif pilih_admin == 5 :
            return main()

def main() :
    while True:
        print("""
Menu Toko Buku dan Alat Tulis
1. Isi keranjang
2. Hapus isi keranjang
3. Ganti nama
4. Lihat isi keranjang
5. Bayar
6. Admin""")
        
        pilih_menu = int(input("\nMasukkan Pilihan Anda : "))

        if pilih_menu == 1:
            masuk_barang_ke_keranjang()

        elif pilih_menu == 2:
            hapus_barang_dari_keranjang()

        elif pilih_menu == 3:
            ganti_nama_barang()

        elif pilih_menu == 4:
            tampil_isi_keranjang()

        elif pilih_menu == 5:
            if isi_keranjang:
                print("Pilih metode pembayaran")
                print("\n1. Cash")
                print("2. Debit")
                metode_bayar = int(input("Masukkan metode pembayaran : "))

                if metode_bayar == 1 :
                    bayar_tunai()

                elif metode_bayar == 2 :
                    debit()
            
            else :
                print("Barang kosong!")
                return main()

        elif pilih_menu == 6 :
            admin()
      
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

main()