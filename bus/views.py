from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render
from . import models

class HomePageView(TemplateView):
    template_name = 'bus/index.html'
    
def destination(request):
    all_destinations = models.Destination.objects.all()
    return render(request, 'bus/destination.html',{'destinations': all_destinations})