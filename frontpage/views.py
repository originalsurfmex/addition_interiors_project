from django.shortcuts import render #get_object_or_404
from django.http import HttpResponseRedirect
# from django.views import generic

from frontpage.models import Slider, Marketing, Feature
from frontpage.forms import ContactForm

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

    context = {'sliders': all_sliders, 'marketing': all_marketing,
               'feature': all_features,
               }
    return render(request, 'frontpage/home.html', context)


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'contact.html', {
        'form': form,
    })
