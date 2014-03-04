from django import forms
from django.contrib import admin

from frontpage.models import Title, Slider

# Register your models here.


class TitleAdmin(admin.ModelAdmin):

    # remove "add" button
    def has_add_permission(self, request):
        return False

    fieldsets = [
        ('20 Character Limit', {'fields': ['title']}),
    ]


class SliderAdmin(admin.ModelAdmin):

    # remove "add" button
    def has_add_permission(self, request):
        return False

    fieldsets = [
        (None,  {'fields': ['slider_title']}),
        (None,  {'fields': ['slider_text']}),
        (None,  {'fields': ['slider_order']}),
    ]
    list_display = ('slider_title', 'slider_text', 'slider_order', )


class SliderForm(forms.ModelForm):

    class Meta:
        model = Slider

admin.site.register(Title, TitleAdmin)
admin.site.register(Slider, SliderAdmin)
