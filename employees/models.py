from django.db import models

class employees(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    address=models.TextField()
    phone=models.BigIntegerField()

    def __str__(self):
        return self.name
