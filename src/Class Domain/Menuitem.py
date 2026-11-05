class MenuItem:
    jumlah_menu = 0                                   # class attribute

    def __init__(self, kode, nama, harga):
        self._kode = kode                             # protected
        self._nama = nama                             # protected
        self.__harga = 0                              # private
        self.harga = harga                            # lewat setter (validasi)
        MenuItem.jumlah_menu += 1

    @property
    def kode(self):
        return self._kode

    @property
    def nama(self):
        return self._nama

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, nilai):
        if not MenuItem.validasi_harga(nilai):
            raise ValueError("Harga harus angka lebih dari 0")
        self.__harga = nilai

    @staticmethod
    def validasi_harga(nilai):
        return isinstance(nilai, (int, float)) and nilai > 0

    @classmethod
    def dari_string(cls, teks):                       # alternative constructor
        kode, nama, harga = teks.split("|")
        return cls(kode, nama, int(harga))

    def hitung_harga(self):
        return self.__harga

    def __str__(self):
        return f"{self._kode} - {self._nama} (Rp{self.hitung_harga():,})"

    def __repr__(self):
        return f"MenuItem({self._kode!r}, {self._nama!r}, {self.__harga})"

    def __eq__(self, other):
        return isinstance(other, MenuItem) and self._kode == other._kode

    def __hash__(self):
        return hash(self._kode)
