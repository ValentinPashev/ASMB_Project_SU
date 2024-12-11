from django import forms
from django.forms import models, formset_factory

from events.mixins import DisableFieldsMixin
from events.models import Event, Comment, EventReport


class EventBaseForm(models.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description', 'branch', 'type_of_event', 'is_online']



class CreateEventForm(EventBaseForm):
    pass

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=35,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a event',
            }
        )
    )


class EventDetailsForm(EventBaseForm):
    pass

class EditEventForm(EventBaseForm):
    pass

class DeleteEventForm(EventBaseForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content')

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required. Write it!',
            },
            'content': {
                'required': 'Content is required. Write it!',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['author'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Your name',
        })

        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Add message...',
            'rows': 1,
        })

CommentFormSet = formset_factory(CommentForm, extra=1)


class EventReportForm(forms.ModelForm):
    class Meta:
        model = EventReport
        fields = ['name','number_of_days', 'organizers', 'prepared', 'attended',   'participated_actively',
                  'points_for_organizers',
                  'points_for_prepared',
                  'points_for_attended',
                  'points_for_participated_actively',
                  ]

        widgets = {
            'organizers': forms.TextInput(attrs={
                'placeholder': 'example: test1@abv.bg test2@gamil.com test3@yahoo.com',
                'title': 'the emails must be splited by space! There can maximum 3 people!'
            }),
            'prepared': forms.TextInput(attrs={
                'placeholder': 'example: test1@abv.bg test2@gamil.com test3@yahoo.com',
                'title': 'the emails must be splited by space! There can maximum 1 person!'
            }),
            'attended': forms.TextInput(attrs={
                'placeholder': 'example: test1@abv.bg test2@gamil.com test3@yahoo.com',
                'title': 'the emails must be splited by space!'
            }),
            'participated_actively': forms.TextInput(attrs={
                'placeholder': 'example: test1@abv.bg test2@gamil.com test3@yahoo.com',
                'title': 'the emails must be splited by space!'
            }),
        }

