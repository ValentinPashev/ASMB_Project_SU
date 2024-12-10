from django.urls import path
from common import views
from common.views import IndexView, ASMPlovdivView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('asmb_sofia/', views.display_asmb_sofia_info, name='asmb_sofia'),
    path('asmb_varna/', views.display_asmb_varna_info, name='asmb_varna'),
    path('asmb_pleven/', views.display_asmb_pleven_info, name='asmb_pleven'),
    path('asmb_burgas/', views.display_asmb_burgas_info, name='asmb_burgas'),
    path('asmb_stara-zagora/', views.display_asmb_stara_zagora_info, name='asmb_stara-zagora'),
    path('asmb_plovdiv/', ASMPlovdivView.as_view(), name='asmb_plovdiv'),
    path('asmb-sofia-university/', views.display_asmb_sofia_university_info, name='asmb_sofia_university'),
]