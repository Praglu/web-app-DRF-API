from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ViewModel(models.Model):
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    email = models.EmailField(null=False)
    password = models.TextField()
    