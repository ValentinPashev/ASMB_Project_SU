from django.contrib.auth import get_user_model
from django.shortcuts import render
from accounts.models import Profile
from campaigns.forms import CampaingReportForm
from campaigns.models import Campaign



# Create your views here.

def pass_campaign_report(request):
    if request.method == 'POST':
        form = CampaingReportForm(request.POST)
        if form.is_valid():
            campaign = form.save()
            distribute_points_from_campaign(campaign)

            form = CampaingReportForm()
            context = {'form': form, 'success': 'Campaign report submitted and points distributed!'}
        else:

            context = {'form': form}
    else:
        form = CampaingReportForm()
        context = {'form': form}

    return render(request, 'campaign_form.html', context)




def distribute_points_from_campaign(campaign):

    if not isinstance(campaign, Campaign):
        raise ValueError("The campaign argument must be a Campaign instance.")

    if campaign.completed:
        print("Campaign already completed. No points distributed.")
        return
    User = get_user_model()
    organizers = campaign.organizers.split(', ')  # Assuming a string of comma-separated emails

    for email in organizers:
        try:
            user = User.objects.get(email=email)
            profile = Profile.objects.get(user=user)
            profile.points_from_events += campaign.points_for_attended
            profile.save()
            print(f"Distributed {campaign.points_for_attended} points to {email}.")
        except User.DoesNotExist:
            print(f"User with email {email} does not exist.")
        except Profile.DoesNotExist:
            print(f"Profile for user with email {email} does not exist.")

    campaign.completed = True
    campaign.save()


