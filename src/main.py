if __name__ == "__main__":
    harga_latte = 22000
    try:
        latte = Minuman("MN01", "Latte", harga_latte, "L", "dingin")
    except ValueError as e:
        print("Validasi:", e)            # nilai salah: berhenti di sini
    else:                                # nilai benar: transaksi dijalankan
        mie = Makanan("MK01", "Mie Pedas", 18000, 4)
        budi = Member("Budi")
        kasir = Kasir("Sari")
        pesanan = kasir.buat_pesanan(budi)
        pesanan.tambah_item(latte, 2)
        pesanan.tambah_item(mie, 1)
        print(latte == MenuItem.dari_string("MN01|Latte|22000"))
        print(latte == mie)
        print(pesanan)
        poin = pesanan.selesaikan()
        print("Poin didapat:", poin)
        print(budi)
        print([k.__name__ for k in Member.__mro__])
    finally:                             # selalu dijalankan, berhasil maupun gagal
        print("Program kasir selesai dijalankan.")
