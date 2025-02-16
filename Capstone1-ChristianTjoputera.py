###Tugas Capstone Project Module-1 ==>Christian Tjoputera(kelas JCDSOL-018 Group 2)
###Case Study yang dipilih ==> Data Karyawan perusahaan
###Goals ==> bisa melakukan proses CRUD,dan ditambahkan beberapa validasi

###BEGIN OF CODE####
# Inisiasi data awal untuk dictionary
karyawan = {
    "1": {"nama": "Christian","usia":40,"divisi":"Sales", "jabatan": "Staff","status": "Kontrak", "gaji": 15000000},
    "2": {"nama": "Jerry","usia":30,"divisi":"Marketing", "jabatan": "Asisten Manager","status": "Tetap", "gaji": 20000000},
    "3": {"nama": "Tina Toon","usia":25,"divisi":"Logistik", "jabatan": "Staff","status": "Kontrak", "gaji": 10000000},
    "4": {"nama": "Rudy Tan","usia":55,"divisi":"HC", "jabatan": "Manager","status": "Tetap", "gaji": 40000000},
}
# Fungsi untuk Menu Utama
def menu_utama():
    print("====Data Registrasi Karyawan PT. XYZ====")
    print("Menu Utama:")
    print("1. Tampilkan data karyawan")
    print("2. Tambahkan data karyawan")
    print("3. Update data karyawan")
    print("4. Hapus data karyawan")
    print("5. Keluar")
    print("============Selamat Datang==============")


# Fungsi untuk menampilkan semua data karyawan
def tampilkan_semuadata():
    print("Data Karyawan:")
    for id_karyawan, data_karyawan in karyawan.items():
        print(f"ID: {id_karyawan}, Nama: {data_karyawan['nama']},Usia: {data_karyawan['usia']},Divisi: {data_karyawan['divisi']}, Jabatan: {data_karyawan['jabatan']},Status: {data_karyawan['status']}, Gaji: {data_karyawan['gaji']}")

# Fungsi untuk menampilkan data karyawan tertentu
def tampilkan_data_tertentu():
    id_karyawan = input("Masukkan ID karyawan yang ingin ditampilkan: ")
    if id_karyawan in karyawan:
        print(f"Data Karyawan dengan ID {id_karyawan}:")
        print(f"Nama: {karyawan[id_karyawan]['nama']},Usia: {karyawan[id_karyawan]['usia']},Divisi: {karyawan[id_karyawan]['divisi']}, Jabatan: {karyawan[id_karyawan]['jabatan']},Status: {karyawan[id_karyawan]['status']}, Gaji: {karyawan[id_karyawan]['gaji']}")
    else:
        print("ID karyawan tidak ditemukan!")

# Fungsi untuk menambahkan data karyawan
def tambahkan_data(dictionary):   
    while True:
        id_karyawan = input("Masukkan ID karyawan: ")
        if id_karyawan in dictionary:
            print("ID karyawan sudah ada, silakan masukkan ID karyawan lain.")
        else:
            nama = input("Masukkan nama karyawan: ").title()
            while True:
                    try:
                        usia = int(input("Masukkan usia karyawan: "))
                        if usia < 0:
                            print("Usia tidak boleh negatif.")
                        else:
                            break
                    except ValueError:
                            print("Usia yang di input harus berupa angka")
            divisi = input("Masukkan divisi karyawan: ").title()
            jabatan = input("Masukkan jabatan karyawan: ").title()
            status = input("Masukkan status karyawan: ").title()
            while True:
                try:
                    gaji = float(input("Masukkan gaji karyawan: "))
                    if gaji < 0:
                        print("Gaji tidak boleh negatif.")
                    else:
                        break
                except ValueError:
                    print("Gaji yang dinput harus berupa angka.")
            break        
    #tanyakan dulu apakah mau disimpan atau tidak ?
    print("Apakah data karyawan akan disimpan ?")
    print("1. Ya")
    print("2. Tidak")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == '1':
        karyawan[id_karyawan] = {"nama": nama,"usia": usia,"divisi" : divisi, "jabatan": jabatan,"status": status, "gaji": gaji}
        print("Data karyawan berhasil ditambahkan!")
    elif pilihan == '2':
        print("Data karyawan tidak disimpan.")
    else:
        print("Pilihan tidak valid!")

   
# Fungsi untuk mengupdate data karyawan
def update_data():
    tampilkan_semuadata()
    id_karyawan = input("Masukkan ID karyawan yang ingin diupdate: ")
    if id_karyawan in karyawan:
        
        nama = input("Masukkan nama karyawan baru: ").title()
        while True:
            try:
                usia = int(input("Masukkan usia karyawan baru: "))
                if usia < 0:
                    print("Usia tidak boleh negatif")
                else:
                    break
            except ValueError:
                    print("Usia yang di input harus berupa angka")
        
        divisi = input("Masukkan divisi karyawan baru: ").title()
        jabatan = input("Masukkan jabatan karyawan baru: ").title()
        status = input("Masukkan status karyawan baru: ").title()
        while True:
            try:
                gaji = float(input("Masukkan gaji karyawan: "))
                if gaji < 0:
                    print("Gaji tidak boleh negatif")
                else:
                    break
            except ValueError:
                print("Gaji yang dinput harus berupa angka.")
        #tanyakan dulu apakah mau dihapus atau tidak ?
        print("Apakah anda yakin data karyawan akan diupdate ?")
        print("1. Ya")
        print("2. Tidak")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            karyawan[id_karyawan] = {"nama": nama,"usia": usia,"divisi": divisi, "jabatan": jabatan,"status": status, "gaji": gaji}
            print(f"Data karyawan berhasil diupdate!")
        elif pilihan == '2':
            print("Data karyawan batal di update.")
        else:
            print("Pilihan tidak valid!")   
        
    else:
        print("ID karyawan tidak ditemukan!")

# Fungsi untuk menghapus data karyawan
def hapus_data():
    tampilkan_semuadata()
    id_karyawan = input("Masukkan ID karyawan yang ingin dihapus: ")
    if id_karyawan in karyawan:
        #tanyakan dulu apakah mau dihapus atau tidak ?
        print("Apakah anda yakin data karyawan akan dihapus ?")
        print("1. Ya")
        print("2. Tidak")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            delid = karyawan[id_karyawan]
            del karyawan[id_karyawan]
            print("Data karyawan berhasil dihapus!")
        elif pilihan == '2':
            print("Data karyawan batal dihapus.")
        else:
            print("Pilihan tidak valid!")   
    else:
        print("ID karyawan tidak ditemukan!")

# Menu utama
while True:
    menu_utama()
    pilihan = input("Masukkan pilihan yang ingin anda lakukan: ")
    if pilihan == '1':
        print("Silahkan Memilih data karyawan yang ingin ditampilkan :")
        print("1. Tampilkan seluruh data karyawan")
        print("2. Tampilkan data karyawan tertentu")
        print("3. Kembali ke menu utama")
        pilihan_tampilkan = input("Masukkan pilihan : ")
        if pilihan_tampilkan == '1':
            tampilkan_semuadata()
        elif pilihan_tampilkan == '2':
            tampilkan_data_tertentu()
        elif pilihan_tampilkan == '3':
            menu_utama()
        else:
            print("Pilihan tidak valid!")
    elif pilihan == '2':
        tambahkan_data(karyawan)
    elif pilihan == '3':
        update_data()
    elif pilihan == '4':
        hapus_data()
    elif pilihan == '5':
        break
    else:
        print("Pilihan yang anda masukkan tidak valid!")

####END OF CODE####
