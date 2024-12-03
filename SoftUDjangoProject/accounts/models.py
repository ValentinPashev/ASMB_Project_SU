from django.contrib.auth.models import AbstractUser
from django.db import models
from SoftUDjangoProject.accounts.choices import BranchChoices


class CustomStudent(AbstractUser):

    faculty_number = models.CharField(
        max_length=25,
        unique=True,
        default='',
    )

    branch = models.CharField(
        max_length=25,
        choices=BranchChoices.choices,
        default=BranchChoices.ASMB_SU
    )


class Profile(models.Model):
    user = models.OneToOneField(
        CustomStudent,
        on_delete=models.CASCADE,
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    faculty_number = models.CharField(
        max_length=25,
        unique=True,
        default='',
    )

    branch = models.CharField(
        max_length=25,
        choices=BranchChoices.choices,
        default=BranchChoices.ASMB_SU
    )

    points_from_events = models.IntegerField(
        default=0
    )

