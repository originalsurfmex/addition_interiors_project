from django import forms
from django.contrib import admin

# these two are added for formfield_overrides
from django.forms import TextInput, Textarea, Select
from django.db import models

from frontpage.models import Title, Slider

# Register your models here.


class TitleAdmin(admin.ModelAdmin):

    # remove "add" button if one field is present
    def has_add_permission(self, request):
        if len(Title.objects.all()) >= 1:
            return False
        else:
            return True

    fieldsets = [
        ('20 Character Limit', {'fields': ['title']}),
    ]
    list_display = ('title', 'link',)
    list_display_links = ('link',)
    list_editable = ('title',)


class SliderAdmin(admin.ModelAdmin):

    # remove "add" button after 3 fields are present
    def has_add_permission(self, request):
        if len(Slider.objects.all()) >= 3:
            return False
        else:
            return True
    
    fieldsets = [
        (None,  {'fields': ['slider_title']}),
        (None,  {'fields': ['slider_text']}),
        (None,  {'fields': ['slider_image']}),
        (None,  {'fields': ['slider_order']}),
    ]

    list_display = (
        'slider_title', 'slider_text', 'slider_order', 'slider_image', 'link',)
    list_display_links = ('link',)
    list_editable = (
        'slider_title', 'slider_text', 'slider_order', 'slider_image',)
    exclude = ('link',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, })},
        # models.PositiveSmallIntegerField: {'widget':
        # forms.Select(attrs={'columns': 10, })},
    }


admin.site.register(Title, TitleAdmin)
admin.site.register(Slider, SliderAdmin)
