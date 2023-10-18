from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Profile

class ProfileListView(ListView):
    model = Profile
    template_name = 'profile_list.html'  # Create this template

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile_detail.html'  # Create this template
