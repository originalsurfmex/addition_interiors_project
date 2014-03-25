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

    if request.method == 'POST' and request.POST['action'] == 'email':
        emailform = ContactForm(request.POST)
        if emailform.is_valid():
            subject = 'ADDITION INTERIORS CONTACT FORM: ' + emailform.cleaned_data['subject']
            message = emailform.cleaned_data['message']
            sender = emailform.cleaned_data['sender']
            phone = emailform.cleaned_data['phone']
            full_message = message + '\n' + 'sent from: ' + \
                sender + '\n' + 'phone number: ' + phone + '\n'

            recipients = ['xxxxxxxxxxxxxxx@gmail.com']
            send_mail(subject, full_message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        emailform = ContactForm()

    if request.method == 'POST' and request.POST['action'] == 'sms':
        smsform = SMSForm(request.POST)
        if smsform.is_valid():
            subject = 'ADDITION INTERIORS TEXT MESSAGE: ' + smsform.cleaned_data['subject']
            message = smsform.cleaned_data['message']
            sender = smsform.cleaned_data['sender']
            cell = smsform.cleaned_data['phone']
            full_message = message + '\n' + 'sent from: ' + \
                sender + '\n' + 'phone number: ' + cell + '\n'

            recipients = ['xxxxxxxxxxxxxxx@gmail.com']
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        smsform = SMSForm()

    context = {'sliders': all_sliders, 'marketing': all_marketing,
               'feature': all_features, 'skills': skill_set,
               # remove this clunky form dict
               'emailform': emailform, 'smsform': smsform,
               }
    return render(request, 'frontpage/home.html', context)


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
