class ItemPesanan:
    def __init__(self, menu, jumlah):
        self.__menu = menu                            # association ke MenuItem
        self.__jumlah = 1
        self.jumlah = jumlah

    @property
    def menu(self):
        return self.__menu

    @property
    def jumlah(self):
        return self.__jumlah

    @jumlah.setter
    def jumlah(self, nilai):
        if not (1 <= nilai <= 20):
            raise ValueError("Jumlah harus 1 sampai 20")
        self.__jumlah = nilai

    def hitung_subtotal(self):
        return self.__menu.hitung_harga() * self.__jumlah

    def __str__(self):
        return f"{self.__jumlah} x {self.__menu.nama} = Rp{self.hitung_subtotal():,}"
