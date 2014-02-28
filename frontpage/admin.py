from django.contrib import admin

from frontpage.models import Title, Slider

# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('20 Character Limit', {'fields': ['title']}),
    ]


class SliderAdmin(admin.ModelAdmin):
    fieldsets =[
        (None,  {'fields':['slider_title']}),
        (None,  {'fields':['slider_text']}),
        (None,  {'fields':['slider_order']}),
    ]
    list_display = ('slider_order', 'slider_title', 'slider_text')

admin.site.register(Title, TitleAdmin)
admin.site.register(Slider, SliderAdmin)
