from datetime import datetime

from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context = {
                'time_now': datetime.now(),
                'user': self.request.user.first_name,
            }

            return context

        context = {
            'time_now': datetime.now(),
        }

        return context

    def get_template_names(self):
        if self.request.user.is_authenticated:
            return ['common/index_logged_in.html']

        else:
            return ['common/index.html']