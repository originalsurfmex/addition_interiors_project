from django.shortcuts import render, get_object_or_404
# from django.views import generic

from frontpage.models import Title, Slider

# Create your views here.


def base_page(request):
    site_title = Title.objects.all()

    context = {'title': site_title }
    return render(request, 'frontpage/base.html', context)


def home_page(request):
    all_sliders = Slider.objects.all()

    context = { 'sliders': all_sliders, }
    return render(request, 'frontpage/home.html', context)
