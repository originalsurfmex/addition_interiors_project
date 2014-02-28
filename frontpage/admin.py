from django.contrib import admin

from frontpage.models import Title, Slider

# Register your models here.


class TitleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('20 Character Limit', {'fields': ['title']}),
    ]


class SliderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Title, TitleAdmin)
admin.site.register(Slider, SliderAdmin)
