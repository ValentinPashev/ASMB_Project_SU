from django.http import HttpResponseRedirect
from django.shortcuts import  render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomStudentFrom, ProfileCreationForm


class RegisterView(CreateView):
    form_class = CustomStudentFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


def create_profile_or_display_view(request):
    profile = request.user.profile

    is_profile_complete = all([
        profile.first_name,
        profile.last_name,
        profile.branch,
    ])

    if is_profile_complete:
        activity_logs = profile.activity_logs.all()
        context = {
            'profile': profile,
            'activity_logs': activity_logs,
        }
        return render(request, 'accounts/profile_details.html', context)

    else:
        if request.method == 'POST':
            form = ProfileCreationForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('profile'))
        else:
            form = ProfileCreationForm(instance=profile)
            print(form.errors)

        context = {
            'form': form,
        }
        return render(request, 'accounts/complete_profile_page.html', context)

