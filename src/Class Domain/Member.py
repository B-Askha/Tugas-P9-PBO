class Member(Pelanggan, PoinMixin):                   # multiple inheritance + mixin
    def proses_pembelian(self, total):                # override
        poin_baru = total // 10000
        self.tambah_poin(poin_baru)
        return poin_baru

    def __str__(self):
        return f"Member {self.nama} (poin: {self.poin})"
