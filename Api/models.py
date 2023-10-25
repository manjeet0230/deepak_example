from django.db import models


class studentmodel(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    roll=models.IntegerField()

    