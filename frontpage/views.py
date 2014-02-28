from django.shortcuts import render, get_object_or_404
# from django.views import generic

from frontpage.models import Title

# Create your views here.


def home_page(request):
    return render(request, 'frontpage/home.html')
