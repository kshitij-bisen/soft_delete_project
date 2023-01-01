from django.db import models

# Create your models here.

class SoftDelete(models.Model):
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract =True

class ColorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class Color(SoftDelete):
    color_name = models.CharField(max_length=100)
    color_hex_code = models.CharField(max_length=100)

    objects = models.Manager()
    color_obj = ColorManager()

    def __str__(self):
        return self.color_name