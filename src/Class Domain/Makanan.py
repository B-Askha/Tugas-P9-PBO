class Makanan(MenuItem):
    def __init__(self, kode, nama, harga, level_pedas=0):
        super().__init__(kode, nama, harga)
        self.__level_pedas = 0
        self.level_pedas = level_pedas

    @property
    def level_pedas(self):
        return self.__level_pedas

    @level_pedas.setter
    def level_pedas(self, nilai):
        if not (0 <= nilai <= 5):
            raise ValueError("Level pedas harus 0 sampai 5")
        self.__level_pedas = nilai

    def hitung_harga(self):                           # override
        total = super().hitung_harga()
        if self.__level_pedas >= 4:
            total += 2000
        return total

    def __str__(self):
        return f"{super().__str__()} [pedas {self.__level_pedas}]"
