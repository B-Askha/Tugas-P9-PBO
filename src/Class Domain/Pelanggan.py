class Pelanggan:
    def __init__(self, nama):
        super().__init__()
        self.__nama = ""
        self.nama = nama

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):
        if not nilai.strip():
            raise ValueError("Nama tidak boleh kosong")
        self.__nama = nilai

    def proses_pembelian(self, total):
        return 0                                      # pelanggan biasa: tanpa poin

    def __str__(self):
        return f"Pelanggan {self.__nama}"
