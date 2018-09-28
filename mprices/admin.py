from django.contrib import admin
from .models import Location, Brand, Phone
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Location)


class BrandAdmin(admin.ModelAdmin):
	search_fields = ['brand_name']

admin.site.register(Brand, BrandAdmin)



class PhoneAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'    
    list_display = ('phone_model', 'price', 'release', 'brand_name')
    autocomplete_fields = ['brand_name']

admin.site.register(Phone, PhoneAdmin)