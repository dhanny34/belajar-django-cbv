from django.db import models
from django.urls import reverse


# Create your models here.
class Sekolah(models.Model):
    nama = models.CharField(max_length=200)
    kepsek = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

    # url setelah selesai post akan redirect kemana
    def get_absolute_url(self):
        return reverse('basic_app:sekolahdetail', kwargs={'pk': self.pk})



class Murid(models.Model):
    nama = models.CharField(max_length=200)
    umur = models.PositiveIntegerField()
    sekolah = models.ForeignKey(Sekolah, related_name='siswa', on_delete=models.CASCADE)

    def __str__(self):
        return self.nama