class Pesanan:
    jumlah_pesanan = 0                                # class attribute

    def __init__(self, pelanggan):
        if not isinstance(pelanggan, Pelanggan):
            raise TypeError("Pesanan harus dibuat untuk objek Pelanggan")
        Pesanan.jumlah_pesanan += 1
        self.__nomor = Pesanan.jumlah_pesanan
        self.__pelanggan = pelanggan                  # aggregation (dari luar)
        self.__daftar_item = []                       # composition (dibuat di dalam)
        self.__selesai = False

    @property
    def nomor(self):
        return self.__nomor

    @property
    def selesai(self):
        return self.__selesai

    def tambah_item(self, menu, jumlah):
        if self.__selesai:                                        # AB-07
            raise PesananSudahSelesaiError(self.__nomor, "ditambah item")
        if not isinstance(menu, MenuItem):
            raise TypeError("Item pesanan harus berupa MenuItem")
        if not menu.tersedia:                                     # AB-06
            raise MenuTidakTersediaError(menu.kode, "sedang habis")
        self.__daftar_item.append(ItemPesanan(menu, jumlah))      # AB-05 dicek di ItemPesanan

    def hitung_total(self):
        return sum(item.hitung_subtotal() for item in self.__daftar_item)

    def selesaikan(self, uang_dibayar):
        """Membayar pesanan. Mengembalikan (kembalian, poin_didapat)."""
        if self.__selesai:                                        # AB-07
            raise PesananSudahSelesaiError(self.__nomor, "dibayar lagi")
        if not self.__daftar_item:                                # AB-08
            raise PesananKosongError(self.__nomor)
        _wajib_angka(uang_dibayar, "Uang yang dibayarkan")
        total = self.hitung_total()
        if uang_dibayar < total:                                  # AB-09
            raise PembayaranKurangError(total, uang_dibayar)
        self.__selesai = True
        poin = self.__pelanggan.proses_pembelian(total)
        return uang_dibayar - total, poin

    def __str__(self):
        status = "LUNAS" if self.__selesai else "BELUM BAYAR"
        baris = [f"Pesanan #{self.__nomor} - {self.__pelanggan.nama} [{status}]"]
        baris += [f"  {item}" for item in self.__daftar_item]
        baris.append(f"  TOTAL = Rp{self.hitung_total():,}")
        return "\n".join(baris)
