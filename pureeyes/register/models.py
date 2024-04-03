from django.db import models

class Customer(models.Model):
    owner_name = models.CharField(max_length=100)
    animal_name = models.CharField(max_length=100)
    animal_age = models.IntegerField()
    animal_type = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    notes = models.TextField()

    class Meta:
        app_label = 'register'

    def __str__(self):
        return self.animal_name
