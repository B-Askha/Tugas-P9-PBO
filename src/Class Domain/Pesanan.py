class Pesanan:
    jumlah_pesanan = 0                                # class attribute

    def __init__(self, pelanggan):
        Pesanan.jumlah_pesanan += 1
        self.nomor = Pesanan.jumlah_pesanan
        self.__pelanggan = pelanggan                  # aggregation (dari luar)
        self.__daftar_item = []                       # composition (dibuat di dalam)
        self.__selesai = False

    def tambah_item(self, menu, jumlah):
        self.__daftar_item.append(ItemPesanan(menu, jumlah))

    def hitung_total(self):
        return sum(item.hitung_subtotal() for item in self.__daftar_item)

    def selesaikan(self):
        if self.__selesai:
            raise ValueError("Pesanan sudah selesai")
        if not self.__daftar_item:
            raise ValueError("Pesanan masih kosong")
        self.__selesai = True
        return self.__pelanggan.proses_pembelian(self.hitung_total())

    def __str__(self):
        baris = [f"Pesanan #{self.nomor} - {self.__pelanggan.nama}"]
        baris += [f"  {item}" for item in self.__daftar_item]
        baris.append(f"  TOTAL = Rp{self.hitung_total():,}")
        return "\n".join(baris)
