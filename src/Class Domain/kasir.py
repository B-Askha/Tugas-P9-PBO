class Kasir:
    def __init__(self, nama):
        self.nama = nama
        self.__daftar_pesanan = []                    # association ke Pesanan
        self.__transaksi_gagal = 0

    @property
    def daftar_pesanan(self):
        return tuple(self.__daftar_pesanan)           # salinan, tidak bisa diubah dari luar

    @property
    def transaksi_gagal(self):
        return self.__transaksi_gagal

    def buat_pesanan(self, pelanggan):
        pesanan = Pesanan(pelanggan)
        self.__daftar_pesanan.append(pesanan)
        return pesanan

    def proses_pembayaran(self, pesanan, uang_dibayar):
        try:
            return pesanan.selesaikan(uang_dibayar)
        except CoffeeShopError:
            self.__transaksi_gagal += 1               # catat dulu...
            raise   
