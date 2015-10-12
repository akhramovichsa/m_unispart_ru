from django.db import models


class Tvr(models.Model):
    art = models.IntegerField(default=0)
    name = models.CharField(max_length=300)
    kol = models.IntegerField(default=0)
    st = models.IntegerField(default=0)

    def __str__(self):
        return self.name