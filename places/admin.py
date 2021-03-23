from django.contrib import admin
from .models import Hookah, HookahTobacco, HookahType, HookahImage

admin.site.register(Hookah)
admin.site.register(HookahTobacco)
admin.site.register(HookahType)
admin.site.register(HookahImage)

