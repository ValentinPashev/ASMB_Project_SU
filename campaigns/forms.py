from django import forms
from campaigns.models import Campaign


class CampaingReportForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = '__all__'
        exclude = ['completed']