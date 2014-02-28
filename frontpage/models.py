from django.db import models

# Create your models here.


class Home(models.Model):
    placeholder = 'placeholder'

    def __str__(self):
        return self.placeholder


class Slider(models.Model):
    slider_text = models.CharField(max_length=200)
    slider_title = models.CharField(max_length=20)
