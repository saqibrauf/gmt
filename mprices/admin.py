from django.contrib import admin
from .models import Location, Brand, Phone
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Location)
admin.site.register(Brand)


class PhoneAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'    
    list_display = ('phone_model', 'price', 'release', 'brand_name')

admin.site.register(Phone, PhoneAdmin)