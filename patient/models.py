from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=254, unique=True)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    disease = models.CharField(max_length=254)
    doctor_name = models.CharField(max_length=128)
    doctor_fees = models.IntegerField(default=500)
    medicine_start_date = models.DateField()

    def __str__(self):
        return self.first_name+" "+self.last_name
