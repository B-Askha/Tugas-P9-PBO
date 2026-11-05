class Minuman(MenuItem):
    TAMBAHAN_UKURAN = {"S": 0, "M": 3000, "L": 6000}  # class attribute

    def __init__(self, kode, nama, harga, ukuran="M", suhu="panas"):
        super().__init__(kode, nama, harga)
        self.__ukuran = "M"
        self.ukuran = ukuran
        self.suhu = suhu

    @property
    def ukuran(self):
        return self.__ukuran

    @ukuran.setter
    def ukuran(self, nilai):
        if nilai not in Minuman.TAMBAHAN_UKURAN:
            raise ValueError("Ukuran harus S, M, atau L")
        self.__ukuran = nilai

    def hitung_harga(self):                           # override
        total = super().hitung_harga() + Minuman.TAMBAHAN_UKURAN[self.__ukuran]
        if self.suhu == "dingin":
            total += 2000
        return total

    def __str__(self):
        return f"{super().__str__()} [{self.__ukuran}, {self.suhu}]"
