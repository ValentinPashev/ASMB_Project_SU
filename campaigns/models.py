from django.db import models

from accounts.choices import BranchChoices
from campaigns.choices import CampaginChoices


# Create your models here.

class Campaign(models.Model):
    name = models.CharField(
        max_length=100
    )

    type_of_campaing = models.CharField(
        choices=CampaginChoices.choices,
        max_length=100,
        default=CampaginChoices.LOCAL
    )

    branch = models.CharField(
        choices=BranchChoices.choices,
        max_length=100,
        default=BranchChoices.ASMB_SU
    )

    number_of_days = models.IntegerField(
        default=0
    )

    organizers = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )

    prepared = models.TextField(
        max_length=35,
        null=True,
        blank=True
    )

    attended = models.TextField(
        max_length=1000,
        null=True,
        blank=True
    )

    presented = models.TextField(
        max_length=350,
        null=True,
        blank=True
    )

    participated_in_preliminary_training = models.TextField(
        max_length=350,
        null=True,
        blank=True
    )

    completed = models.BooleanField(
        default=False
    )

    points_for_organizers = models.IntegerField(
        default=0
    )

    points_for_prepared = models.IntegerField(
        default=0
    )

    points_for_attended = models.IntegerField(
        default=0
    )
    points_for_presented = models.IntegerField(
        default=0
    )
    points_for_participated_in_preliminary_training = models.IntegerField(
        default=0
    )
