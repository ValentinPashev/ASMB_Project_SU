from django import forms
from django.forms import models, formset_factory

from events.mixins import DisableFieldsMixin
from events.models import Event, Comment


class EventBaseForm(models.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'location', 'description', 'created_by']



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

class EditEventForm(EventBaseForm):
    pass

class DeleteEventForm(EventBaseForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)

CommentFormSet = formset_factory(CommentForm, extra=1)