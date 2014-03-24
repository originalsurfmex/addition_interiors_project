from django.shortcuts import render  # get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail  # BadHeaderError

from django.views.generic import ListView, DetailView

from frontpage.models import Slider, Marketing, Feature, Skills, Relationship, Brand, About
from frontpage.forms import ContactForm, SMSForm

# Create your views here.


def home_page(request):
    all_sliders = Slider.objects.all()
    all_marketing = Marketing.objects.all()
    all_features = Feature.objects.all()
    skill_set = Skills.objects.all()
    
    #clunky way of adding the form...no goood
    if request.method == 'POST' and request.POST['action'] == 'email':
        emailform = ContactForm(request.POST)
        if emailform.is_valid():
            return HttpResponseRedirect('frontpage/thanks/')
    else:
        emailform = ContactForm()

    if request.method == 'POST' and request.POST['action'] == 'sms':
        smsform = SMSForm(request.POST)
        if smsform.is_valid():
            return HttpResponseRedirect('frontpage/thanks/')
    else:
        smsform = SMSForm()

    context = {'sliders': all_sliders, 'marketing': all_marketing,
               'feature': all_features, 'skills': skill_set, 
               #remove this clunky form dict
               'emailform': emailform, 'smsform': smsform,
               }
    return render(request, 'frontpage/home.html', context)


def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@additioninteriors.com'),
                # email address where message is sent.
                ['email@additioninteriors.com'],
            )
            return HttpResponseRedirect('frontpage/thanks/')
    return render(request, 'frontpage/contact.html',
                  {'errors': errors})


def sms(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@additioninteriors.com'),
                # email address where message is sent.
                ['sms@additioninteriors.com'],
            )
            return HttpResponseRedirect('frontpage/thanks/')
    return render(request, 'frontpage/sms.html',
                  {'errors': errors})


def thanks(request):
    return render(request, 'frontpage/thanks.html')

# --------------------------------------------------#
# STATIC PAGES - GENERIC TEMPLATES #
# --------------------------------------------------#

class SkillsList(ListView):
    model = Skills

class RelationshipList(ListView):
    model = Relationship


class BrandList(ListView):
    model = Brand

class AboutDetail(ListView):
    model = About
