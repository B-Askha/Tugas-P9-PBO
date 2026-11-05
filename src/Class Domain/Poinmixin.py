class PoinMixin:
    def __init__(self):
        super().__init__()
        self.__poin = 0

    @property
    def poin(self):
        return self.__poin

    def tambah_poin(self, jumlah):
        if jumlah < 0:
            raise ValueError("Poin tidak boleh negatif")
        self.__poin += jumlah
