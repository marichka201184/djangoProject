from django.db import models


# Create your models here.
class Owner(models.Model):
    class Meta:
        db_table = 'owner'
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    name = models.CharField(max_length=30, verbose_name='Name')
    age = models.IntegerField(verbose_name="Age")
    pet_name = models.CharField(max_length=30, verbose_name='Pet')

    def __str__(self):
        return self.name


class Pet(models.Model):
    class Meta:
        db_table = 'pet'
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    name = models.CharField(max_length=30, verbose_name='Name')
    age = models.IntegerField(verbose_name='Age')
    breed = models.CharField(max_length=30, verbose_name='Breed')
    owner_name = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
