from django import forms
from django.contrib import admin

# these two are added for formfield_overrides
from django.forms import TextInput, Textarea, Select
from django.db import models

from frontpage.models import Title, Slider

# Register your models here.


class TitleAdmin(admin.ModelAdmin):

    # remove "add" button
    def has_add_permission(self, request):
        return False

    fieldsets = [
        ('20 Character Limit', {'fields': ['title']}),
    ]
    list_display = ('title', 'link',)
    list_display_links = ('link',)
    list_editable = ('title',)


class SliderAdmin(admin.ModelAdmin):

    # remove "add" button
    # def has_add_permission(self, request):
    #     return False

    if len(Slider.objects.all()) >= 3:
        def has_add_permission(self, request):
            return False
    else:
        def has_add_permission(self, request):
            return True

    fieldsets = [
        (None,  {'fields': ['slider_title']}),
        (None,  {'fields': ['slider_text']}),
        (None,  {'fields': ['slider_order']}),
    ]

    list_display = (
        'slider_title', 'slider_text', 'slider_order', 'link',)
    list_display_links = ('link',)
    list_editable = ('slider_title', 'slider_text', 'slider_order',)
    exclude = ('link',)

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 4, })},
        # models.PositiveSmallIntegerField: {'widget':
        # forms.Select(attrs={'columns': 10, })},
    }


admin.site.register(Title, TitleAdmin)
admin.site.register(Slider, SliderAdmin)
