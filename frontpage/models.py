from django.db import models
from django import forms
from django.core.mail import send_mail

from django.core.exceptions import ValidationError


# ------------------------------------------------------------
# VALIDATIONS
# ------------------------------------------------------------

def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
       # make sure of the correct quantity and allow re-saving existing objects
            obj.id != model.objects.get().id):
        raise ValidationError("only 1 %s can be created" % model.__name__)


def validate_only_three_instances(obj):
    model = obj.__class__
    # make sure of the correct quantity and allow re-saving existing objects
    if (model.objects.count() > 2 and
            model.objects.filter(id=obj.id).exists() == False):
        raise ValidationError("only 3 %ss can be created" % model.__name__)

# ------------------------------------------------------------
# MODELS
# ------------------------------------------------------------


class Title(models.Model):
    title = models.CharField(max_length=20, default='Addition Interiors')

    link = "Edit"

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return self.title


class Slider(models.Model):
    slider_title = models.CharField(max_length=20)
    slider_text = models.TextField(max_length=200)
    slider_order = models.PositiveSmallIntegerField(
        default=1, blank=True, null=True, choices=[(1, 'first'),
                                                   (2, 'middle'), (3, 'last')])
    slider_image = models.ImageField(
        upload_to='media/frontpage/slider', blank=True, null=True,)
    link = "Edit"

    def clean(self):
        validate_only_three_instances(self)

    def __str__(self):
        return self.slider_title


class Marketing(models.Model):
    marketing_title = models.CharField(max_length=20)
    marketing_text = models.TextField(max_length=300)
    marketing_order = models.PositiveSmallIntegerField(
        default=1, blank=True, null=True, choices=[(1, 'first'),
                                                   (2, 'middle'), (3, 'last')])
    marketing_image = models.ImageField(
        upload_to='media/frontpage/marketing', blank=True, null=True,)
    link = "Edit"

    def clean(self):
        validate_only_three_instances(self)

    def __str__(self):
        return self.marketing_title


class Feature(models.Model):
    feature_title = models.CharField(max_length=20)
    feature_subtitle = models.CharField(max_length=20)
    feature_text = models.TextField(max_length=300)
    feature_order = models.PositiveSmallIntegerField(
        default=1, blank=True, null=True, choices=[(1, 'first'),
                                                   (2, 'middle'), (3, 'last')])
    feature_image = models.ImageField(
        upload_to='media/frontpage/feature', blank=True, null=True,)
    link = "Edit"

    def clean(self):
        validate_only_three_instances(self)

    def __str__(self):
        return self.feature_title
