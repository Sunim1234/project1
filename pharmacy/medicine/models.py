from django.db import models

# Create your models here.
class Medicine(models.Model):
    med_name = models.Charfield(max_length=50)
    med_id = models.CharField(max_length=20, unique=True)

     def __str__(self):
        return f"{self.med_id}. {self.med_name}"
