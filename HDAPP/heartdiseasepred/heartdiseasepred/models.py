from django.db import models



class Datas(models.Model):

    age = models.PositiveIntegerField( null=True)
    sex = models.PositiveIntegerField( null=True)
    cp = models.PositiveIntegerField( null=True)
    trestbps = models.PositiveIntegerField( null=True)
    chol = models.PositiveIntegerField( null=True)
    fbs = models.PositiveIntegerField( null=True)
    restecg = models.PositiveIntegerField( null=True)
    thalach = models.PositiveIntegerField( null=True)
    exang = models.PositiveIntegerField( null=True)
    oldpeak = models.FloatField(null=True)
    slope = models.PositiveIntegerField( null=True)
    ca = models.PositiveIntegerField( null=True)
    thal = models.PositiveIntegerField( null=True)
    target = models.PositiveIntegerField( null=True)



    def __str__(self):
        return str(self.target)


class Doctor(models.Model):
    Name = models.CharField(max_length=1000, null=True)
    City = models.CharField(max_length=1000, null=True)
    Qualification = models.CharField(max_length=1000, null=True)
    Address = models.CharField( max_length=1000, null=True)
    Phone = models.CharField( max_length=1000,null=True)
    Hotline= models.CharField( max_length=1000,null=True)
    ConsultingHour= models.CharField(max_length=1000,null=True)
    ConsultingDay = models.CharField(max_length=1000, null=True)

