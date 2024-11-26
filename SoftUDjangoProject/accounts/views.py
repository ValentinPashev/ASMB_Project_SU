from django.urls import reverse_lazy
from django.views.generic import CreateView
from SoftUDjangoProject.forms import CustomStudentFrom


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomStudentFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
