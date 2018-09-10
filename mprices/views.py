from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Location, Brand, Phone

def index(request):
	if request.POST:
		min_price = request.POST.get('min-price', '10000')
		max_price = request.POST.get('max-price', '30000')
		phones = Phone.objects.filter(price__gte=min_price, price__lte=max_price).order_by('-release', '-price')
		total = str(phones.count())
		message = total + ' Search result for mobiles between ' + min_price + ' to ' + max_price
	else:
		phones = Phone.objects.filter(price__gt=0).order_by('-release', '-price')
		message = ''

	sidebar_brands = Brand.objects.all().order_by('brand_name')
	context = {
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
		'message' : message
	}
	return render(request, 'mprices/index.html', context)

def brand(request, slug, location):
	brand = get_object_or_404(Brand, brand_slug=slug)
	phones = brand.phone_set.all().order_by('-release', '-price')
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	sidebar_location = get_object_or_404(Location, location_slug=location)
	context = {
		'brand' : brand,
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
		'sidebar_location' : sidebar_location,
	}
	return render(request, 'mprices/brand.html', context)

def phone(request, slug, location):
	phone = get_object_or_404(Phone, phone_model_slug=slug)
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	brand = phone.brand_name
	sidebar_phones = Phone.objects.filter(brand_name=brand)
	sidebar_location = get_object_or_404(Location, location_slug=location)
	context = {
		'phone' : phone,
		'brand' : brand,
		'sidebar_location' : sidebar_location,
		'sidebar_brands' : sidebar_brands,
		'sidebar_phones' : sidebar_phones,
	}
	return render(request, 'mprices/phone-detail.html', context)