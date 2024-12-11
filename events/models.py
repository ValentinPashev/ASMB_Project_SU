from django.db import models
from accounts.choices import BranchChoices
from accounts.models import Profile
from events.choices import EventChoices


class Event(models.Model):
    name = models.CharField(
        max_length=150
        )

    date = models.DateField(

    )

    location = models.CharField(

    )

    description = models.TextField(
        max_length=300
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    created_by = models.CharField(
        models.ForeignKey(
            Profile,
            on_delete=models.CASCADE
        )
    )

    approved = models.BooleanField(
        default=False
    )

    type_of_event = models.CharField(
        choices=EventChoices.choices,
        max_length=100,
        default=EventChoices.LOCAL
    )

    branch = models.CharField(
        choices=BranchChoices.choices,
        max_length=100,
        default=BranchChoices.ASMB_SU
    )

    completed = models.BooleanField(
        default=False
    )

    is_online = models.BooleanField(
        default=False
    )

    class Meta:
        permissions = [
            ('can_approve_events', 'Can approve event'),
            ('can_make_report', 'Can make report'),
            ('can_see_report', 'Can see report'),
            ('can_edit_report', 'Can edit report'),
        ]
    def __str__(self):
        return self.name



class Comment(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

class EventReport (models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='reports',
    )

    name = models.CharField(
        max_length=150,
        default='Student meeting'
    )

    number_of_days = models.IntegerField(
        default=0
    )

    organizers = models.TextField(
        max_length=100,
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

    participated_actively = models.TextField(
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

    points_for_participated_actively = models.IntegerField(
        default=0
    )

