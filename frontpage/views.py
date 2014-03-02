from django.shortcuts import render, get_object_or_404
# from django.views import generic

from frontpage.models import Title, Slider

# Create your views here.


def base_page(request):
    context = {'title': "TITLE FROM VIEW TEMPLATE"}
    return render(request, 'frontpage/base.html', context)


def home_page(request):
    all_sliders = Slider.objects.all()
    slider_1 = all_sliders[0]

    context = {'placeholder': "PLACEHOLDER TEXT FROM VIEW TEMPLATE", 
        'sliders': all_sliders, 'slider_1': slider_1,
        }
    return render(request, 'frontpage/home.html', context)
