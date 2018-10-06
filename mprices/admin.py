from django.contrib import admin
from .models import Country, Location, Brand, Phone
from django.utils.translation import gettext_lazy as _
from django_summernote.admin import SummernoteModelAdmin



class CountryAdmin(admin.ModelAdmin):
	list_display = ('country', 'currency', 'exchange_rate')
	search_fields = ['country']

class LocatiionAdmin(admin.ModelAdmin):
	list_display = ('location_name', 'country')
	autocomplete_fields = ['country']

class BrandAdmin(admin.ModelAdmin):
	search_fields = ['brand_name']


class PhoneAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'    
    list_display = ('phone_model', 'price', 'release', 'brand_name')
    autocomplete_fields = ['brand_name']
    search_fields = ['phone_model']

admin.site.register(Country, CountryAdmin)
admin.site.register(Location, LocatiionAdmin)
admin.site.register(Phone, PhoneAdmin)
admin.site.register(Brand, BrandAdmin)