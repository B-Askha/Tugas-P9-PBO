class PoinMixin:
    def __init__(self):
        super().__init__()
        self.__poin = 0

    @property
    def poin(self):
        return self.__poin

    def tambah_poin(self, jumlah):                    # AB-10
        _wajib_int(jumlah, "Poin")
        if jumlah < 0:
            raise ValueError(f"Poin tidak boleh negatif, diterima: {jumlah}")
        self.__poin += jumlah
