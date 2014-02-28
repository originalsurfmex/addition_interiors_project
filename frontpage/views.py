from django.shortcuts import render, get_object_or_404
# from django.views import generic

from frontpage.models import Title, Slider

# Create your views here.


def base_page(request):
    context = {'placeholder': "PLACEHOLDER TEXT FROM VIEW TEMPLATE"}
    return render(request, 'frontpage/base.html', context)


def home_page(request):
    context = {'placeholder': "PLACEHOLDER TEXT FROM VIEW TEMPLATE"}
    return render(request, 'frontpage/home.html', context)
