from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Plastic
# Create your views here.

class HomePageView(TemplateView): 
    template_name = 'home.html'
    model = Plastic

class CreatePageView(CreateView): 
    template_name = 'create.html'
    model = Plastic
    fields = "__all__"
    