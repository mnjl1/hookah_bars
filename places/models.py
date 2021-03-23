from django.db import models
from cities_light.models import City
from django.urls import reverse

class HookahType(models.Model):
    hookah_type = models.CharField(max_length = 50, unique = True)


class HookahTobacco(models.Model):
    hookah_tobacco = models.CharField(max_length = 50, unique = True)


class Hookah(models.Model):
    hookah_name = models.CharField(max_length = 200, blank = False)
    city = models.ForeignKey(City, on_delete = models.CASCADE)
    street = models.CharField(max_length = 400, blank = True)
    website = models.URLField(max_length = 420, blank = True)
    # TODO phone number validator with regex
    # TODO add call button
    phone = models.CharField(max_length = 10, blank = True)
    description = models.TextField(blank = True)
    credit_card = models.BooleanField(default = True)
    hookah_type = models.ManyToManyField(HookahType, blank = True)
    hookah_tobacco = models.ManyToManyField(HookahTobacco, blank = True)
    summer_terrace = models.BooleanField(default = False)
    created_at = models.DateField(auto_now_add = True)
    last_modified = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.hookah_name}, {self.city}' 

    # def get_absolute_url(self):
    #     return reverse()


class HookahImage(models.Model):
    hookah_image = models.ImageField(
        upload_to = 'hookahImages'
    )
    hookah = models.ForeignKey(Hookah, on_delete = models.CASCADE)

