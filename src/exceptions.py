"""Hierarki custom exception untuk sistem kasir coffee shop.

Kode aturan bisnis (AB-xx) dijelaskan di README.md.
"""


class CoffeeShopError(Exception):
    """Base exception aplikasi: semua pelanggaran aturan bisnis kasir."""

    def __init__(self, pesan, kode_aturan=None):
        super().__init__(pesan)
        self.kode_aturan = kode_aturan        # konteks: aturan bisnis yang dilanggar


class MenuTidakTersediaError(CoffeeShopError):
    """AB-06: menu tidak ada di daftar menu atau sedang habis."""

    def __init__(self, kode_menu, alasan="tidak ada di daftar menu"):
        self.kode_menu = kode_menu            # konteks
        self.alasan = alasan                  # konteks
        super().__init__(f"Menu '{kode_menu}' {alasan}", "AB-06")


class PesananError(CoffeeShopError):
    """Kelompok error yang berkaitan dengan status sebuah pesanan."""

    def __init__(self, pesan, nomor_pesanan, kode_aturan=None):
        self.nomor_pesanan = nomor_pesanan    # konteks
        super().__init__(pesan, kode_aturan)


class PesananKosongError(PesananError):
    """AB-08: pesanan tanpa item tidak boleh dibayar."""

    def __init__(self, nomor_pesanan):
        super().__init__(
            f"Pesanan #{nomor_pesanan} masih kosong, belum bisa dibayar",
            nomor_pesanan, "AB-08")


class PesananSudahSelesaiError(PesananError):
    """AB-07: pesanan yang sudah dibayar tidak boleh diubah atau dibayar lagi."""

    def __init__(self, nomor_pesanan, aksi):
        self.aksi = aksi                      # konteks: aksi yang ditolak
        super().__init__(
            f"Pesanan #{nomor_pesanan} sudah selesai, tidak bisa {aksi}",
            nomor_pesanan, "AB-07")


class PembayaranKurangError(CoffeeShopError):
    """AB-09: uang yang dibayarkan harus minimal sebesar total pesanan."""

    def __init__(self, total, dibayar):
        self.total = total                    # konteks
        self.dibayar = dibayar                # konteks
        self.kekurangan = total - dibayar     # konteks
        super().__init__(
            f"Uang Rp{dibayar:,} kurang dari total Rp{total:,}", "AB-09")

