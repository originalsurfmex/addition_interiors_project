from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render  # get_object_or_404
from django.http import HttpResponseRedirect
# from django.views import generic

from django.views.generic import TemplateView

from frontpage.models import Slider, Marketing, Feature
from frontpage.forms import EmailForm

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


def sendmail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email'] #send this for contacting back,kl
            subject = form.cleaned_data['subject']
            botcheck = form.cleaned_data['botcheck'].lower()
            message = form.cleaned_data['message']
            if botcheck == 'yes':
                try:
                    fullemail = firstname + " " + \
                        lastname + " " + "<" + email + ">"
                    send_mail(
                        subject, message, fullemail, ['SENDTOUSER@DOMAIN.COM'])
                    return HttpResponseRedirect('/email/thankyou/')
                except:
                    return HttpResponseRedirect('/email/')
        else:
            return HttpResponseRedirect('/email/')
    else:
        return HttpResponseRedirect('/email/')
