from django.db import models


# Create your models here.
class Applicant(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # Determines what would be shown when we print an instance of the class
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
