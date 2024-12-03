from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()

class Student(models.Model):
    full_name = models.CharField(
        max_length=100
    ),

    faculty_number = models.CharField(
        max_length=100
    )

    # user = models.ForeignKey(
    #     to=UserModel,
    #     on_delete=models.CASCADE,
    # )
