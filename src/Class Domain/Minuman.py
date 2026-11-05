class Minuman(MenuItem):
    TAMBAHAN_UKURAN = {"S": 0, "M": 3000, "L": 6000}  # class attribute
    SUHU_VALID = ("panas", "dingin")                  # class attribute

    def __init__(self, kode, nama, harga, ukuran="M", suhu="panas"):
        super().__init__(kode, nama, harga)
        self.__ukuran = "M"
        self.ukuran = ukuran
        self.__suhu = "panas"
        self.suhu = suhu

    @property
    def ukuran(self):
        return self.__ukuran

    @ukuran.setter
    def ukuran(self, nilai):                          # AB-02
        if nilai not in Minuman.TAMBAHAN_UKURAN:
            raise ValueError(f"Ukuran harus S, M, atau L, diterima: {nilai!r}")
        self.__ukuran = nilai

    @property
    def suhu(self):
        return self.__suhu

    @suhu.setter
    def suhu(self, nilai):                            # AB-02 (dulu belum divalidasi)
        if nilai not in Minuman.SUHU_VALID:
            raise ValueError(f"Suhu harus 'panas' atau 'dingin', diterima: {nilai!r}")
        self.__suhu = nilai

    def hitung_harga(self):                           # override
        total = super().hitung_harga() + Minuman.TAMBAHAN_UKURAN[self.__ukuran]
        if self.__suhu == "dingin":
            total += 2000
        return total

    def __str__(self):
        return f"{super().__str__()} [{self.__ukuran}, {self.__suhu}]"
