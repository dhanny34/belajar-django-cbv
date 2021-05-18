from django.db import models

# Create your models here.
class Sekolah(models.Model):
    nama = models.CharField(max_length=200)
    kepsek = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)

    def __str__(self):
        return self.nama


class Murid(models.Model):
    nama = models.CharField(max_length=200)
    umur = models.PositiveIntegerField()
    sekolah = models.ForeignKey(Sekolah, related_name='siswa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama