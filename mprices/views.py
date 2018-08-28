from django.shortcuts import render
from .models import Location, Brand, Phone

def index(request):
	phones = Phone.objects.filter(price__gt=0).order_by('-price')
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	context = {
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
	}
	return render(request, 'mprices/index.html', context)

def coming_soon(request):
	phones = Phone.objects.filter(status='Coming Soon').order_by('-price', 'brand_name')
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	context = {
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
	}
	return render(request, 'mprices/index.html', context)

def brand(request, slug, location):
	brand = Brand.objects.get(brand_slug=slug)
	phones = brand.phone_set.all().order_by('-price')
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	sidebar_location = Location.objects.get(location_slug=location)
	context = {
		'brand' : brand,
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
		'sidebar_location' : sidebar_location,
	}
	return render(request, 'mprices/brand.html', context)

def phone(request, slug, location):
	phone = Phone.objects.get(phone_model_slug=slug)
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	brand = phone.brand_name
	sidebar_phones = Phone.objects.filter(brand_name=brand)
	sidebar_location = Location.objects.get(location_slug=location)
	context = {
		'phone' : phone,
		'brand' : brand,
		'sidebar_location' : sidebar_location,
		'sidebar_brands' : sidebar_brands,
		'sidebar_phones' : sidebar_phones,
	}
	return render(request, 'mprices/phone-detail.html', context)