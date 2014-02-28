from django.db import models

# Create your models here.


class Title(models.Model):
    title = models.CharField(max_length=20, default='Addition Interiors')

    #class Meta:
    #    verbose_name_plural = "Home"

    def __str__(self):
        return self.title


class Slider(models.Model):
    slider_title = models.CharField(max_length=20)
    slider_text = models.CharField(max_length=200)
    slider_order = models.PositiveSmallIntegerField(default=1, blank=True, null=True)

    def __str__(self):
        return self.slider_title
