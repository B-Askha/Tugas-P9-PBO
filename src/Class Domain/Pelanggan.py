class Pelanggan:
    def __init__(self, nama):
        super().__init__()
        self.__nama = ""
        self.nama = nama

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nilai):                            # AB-04
        if not isinstance(nilai, str):
            raise TypeError(f"Nama harus berupa teks, bukan {type(nilai).__name__}")
        if not nilai.strip():
            raise ValueError("Nama pelanggan tidak boleh kosong")
        self.__nama = nilai.strip()

    def proses_pembelian(self, total):
        return 0                                      # pelanggan biasa: tanpa poin

    def __str__(self):
        return f"Pelanggan {self.__nama}"
