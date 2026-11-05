class Kasir:
    def __init__(self, nama):
        self.nama = nama
        self.__daftar_pesanan = []                    # association ke Pesanan

    def buat_pesanan(self, pelanggan):
        pesanan = Pesanan(pelanggan)
        self.__daftar_pesanan.append(pesanan)
        return pesanan
