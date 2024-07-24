from django.db import models

# Create your models here.

class Staffs(models.Model):

    name=models.CharField(max_length=200)

    age=models.PositiveIntegerField()

    place=models.CharField(max_length=200)

    department=models.CharField(max_length=200)

    salary=models.PositiveIntegerField()

    image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):

        return self.name