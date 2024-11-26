from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def student_info(request):
    return HttpResponse('Some student info')