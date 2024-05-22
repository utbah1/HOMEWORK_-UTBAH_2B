import Data_HP

stok = [
    {"nama": "Iphone 15 Purple", "jumlah": 10 },
    {"nama": "Iphone 15 Yellow", "jumlah": 18 },
    {"nama": "Iphone 15 Green", "jumlah": 15 },
    {"nama": "Iphone 15 Blue", "jumlah": 9 },
    {"nama": "Iphone 15 Pink", "jumlah": 6 },
]

def main():
    while True:
        print("\nSelamat Datang Di Program Manajemen stok Handphone")
        print("Menu:")
        print("1. Tambah Data Handphone")
        print("2. Edit Data")
        print("3. Hapus Data Handphone")
        print("4. Cari Data")
        print("5. Tampilkan Data Handphone")
        print("6. Tampilkan Jumlah Data")
        print("7. Keluar")

        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            nama_benda = input("Masukan nama Handphone: ")
            jumlah_benda = int(input("Masukan jumlah Handphone: "))
            tambah = Data_HP.tambah_data_barang(stok, nama_benda, jumlah_benda)
            print("Data berhasil ditambah")

        elif pilihan == "2":
            indeks = int(input("Masukkan indeks data yang ingin diedit: "))
            nama_baru = input("Masukkan nama baru: ")
            jumlah_baru = int(input("Masukkan jumlah baru: "))
            sukses = Data_HP.edit_data(stok, indeks, nama_baru, jumlah_baru)
            if sukses:
                print("Data berhasil diedit.")
            else:
                print("Indeks tidak valid.")

        elif pilihan == "3":
            indeks = int(input("Masukkan indeks data yang ingin dihapus: "))
            berhasil = Data_HP.hapus_data(stok, indeks)
            if berhasil:
                print("Data berhasil dihapus")
            else:
                print("Indeks tidak valid")

        elif pilihan == "4":
            nama = input("Masukkan nama Handphone yang dicari = ")
            hasil = Data_HP.cari_data(stok, nama)
            if hasil:
                print(f"Ditemukan: Nama = {hasil['nama']}, Jumlah = {hasil['jumlah']}")
            else:
                print("Handphone tidak ditemukan.")

        elif pilihan == "5":
            Data_HP.tampilkan_data(stok)

        elif pilihan == "6":
            jumlah_data = Data_HP.hitung_jumlah_data(stok)
            print(f"Jumlah data yang tersimpan = {jumlah_data}")

        elif pilihan == "7":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()