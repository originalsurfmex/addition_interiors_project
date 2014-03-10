from django.shortcuts import render, get_object_or_404
# from django.views import generic

from frontpage.models import Title, Slider, Marketing, Feature

# Create your views here.

"""
def base_page(request):
    site_title = Title.objects.all()

    context = {'title': site_title }
    return render(request, 'frontpage/navbar.html', context)
"""

def home_page(request):
    all_sliders = Slider.objects.all()
    all_marketing = Marketing.objects.all()
    all_features = Feature.objects.all()

    context = { 'sliders': all_sliders, 'marketing': all_marketing,
    			'feature': all_features,
    }
    return render(request, 'frontpage/home.html', context)
