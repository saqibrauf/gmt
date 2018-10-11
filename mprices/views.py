from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Location, Brand, Phone, Country
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	
	phones = Phone.objects.filter(price__gt=0).order_by('-release', '-price')	

	page = request.GET.get('page', 1)
	paginator = Paginator(phones, 30)
	try:
		phones = paginator.page(page)
	except PageNotAnInteger:
		phones = paginator.page(1)
	except EmptyPage:
		phones = paginator.page(paginator.num_pages)	

	sidebar_brands = Brand.objects.all().order_by('brand_name')
	context = {
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
	}
	return render(request, 'mprices/index.html', context)


def search(request):
	if request.GET:
		min_price = request.GET.get('minprice', '100')
		max_price = request.GET.get('maxprice', '250')
		phones = Phone.objects.filter(price__gte=min_price, price__lte=max_price).order_by('-release', '-price')
		total = str(phones.count())
		message = total + ' Search result for mobiles between ' + min_price + ' to ' + max_price

		page = request.GET.get('page', 1)

		paginator = Paginator(phones, 30)
		try:
			phones = paginator.page(page)
		except PageNotAnInteger:
			phones = paginator.page(1)
		except EmptyPage:
			phones = paginator.page(paginator.num_pages)
		

		sidebar_brands = Brand.objects.all().order_by('brand_name')
		context = {
			'phones' : phones,
			'sidebar_brands' : sidebar_brands,
			'message' : message
		}

	else:
		message = ''	
		sidebar_brands = Brand.objects.all().order_by('brand_name')
		context = {
			'sidebar_brands' : sidebar_brands,
			'message' : message
		}
	return render(request, 'mprices/search.html', context)


def brand(request, slug, location=''):
	brand = get_object_or_404(Brand, brand_slug=slug)
	phones = brand.phone_set.all().order_by('-release', '-price')
	sidebar_brands = Brand.objects.all().order_by('brand_name')

	if location:
		sidebar_location = get_object_or_404(Location, location_slug=location)
		try:
			country = Country.objects.get(location__location_slug=location)
			if country.currency != 'USD':
				base_cur = Country.objects.get(currency='USD')
				base = 1 / base_cur.exchange_rate
				er = country.exchange_rate
				exch = base * er
				request.session['currency'] = country.currency
				request.session['exchange'] = float(exch)
				request.session['location'] = location
			else:
				request.session['currency'] = 'USD'
				request.session['exchange'] = int(1)
				request.session['location'] = ''
		except:
			request.session['currency'] = 'USD'
			request.session['exchange'] = int(1)
			request.session['location'] = sidebar_location.location_name
	else:
		sidebar_location = ''
		request.session['currency'] = 'USD'
		request.session['exchange'] = int(1)
		request.session['location'] = ''	

	page = request.GET.get('page', 1)
	paginator = Paginator(phones, 30)
	try:
		phones = paginator.page(page)
	except PageNotAnInteger:
		phones = paginator.page(1)
	except EmptyPage:
		phones = paginator.page(paginator.num_pages)


	context = {
		'brand' : brand,
		'phones' : phones,
		'sidebar_brands' : sidebar_brands,
		'sidebar_location' : sidebar_location,
	}
	return render(request, 'mprices/brand.html', context)

def phone(request, slug, location=''):
	phone = get_object_or_404(Phone, phone_model_slug=slug)
	sidebar_brands = Brand.objects.all().order_by('brand_name')
	brand = phone.brand_name
	sidebar_phones = Phone.objects.filter(brand_name=brand).exclude(id=phone.id).order_by('-release', '-price')
	
	if location:
		sidebar_location = get_object_or_404(Location, location_slug=location)
		try:
			country = Country.objects.get(location__location_slug=location)
			if country.currency != 'USD':
				base_cur = Country.objects.get(currency='USD')
				base = 1 / base_cur.exchange_rate
				er = country.exchange_rate
				exch = base * er
				request.session['currency'] = country.currency
				request.session['exchange'] = float(exch)
				request.session['location'] = location
			else:
				request.session['currency'] = 'USD'
				request.session['exchange'] = int(1)
				request.session['location'] = ''
		except:
			request.session['currency'] = 'USD'
			request.session['exchange'] = int(1)
			request.session['location'] = sidebar_location.location_name
	else:
		sidebar_location = ''
		request.session['currency'] = 'USD'
		request.session['exchange'] = int(1)
		request.session['location'] = ''		

	context = {
		'phone' : phone,
		'brand' : brand,
		'sidebar_location' : sidebar_location,
		'sidebar_brands' : sidebar_brands,
		'sidebar_phones' : sidebar_phones,
	}
	return render(request, 'mprices/phone-detail.html', context)

#AJAX Call for Phone Model
from django.http import JsonResponse
def get_phone(request):
	results = []
	if request.GET:
		query = request.GET.get('term')
		if query:
			p_model = Phone.objects.filter(phone_model__icontains=query)[:8]
			
			for p in p_model:
				url = reverse('phone', kwargs={'slug': p.phone_model_slug})
				if request.session['location']:
					url = url[:-1] + '-in-' + request.session['location']
				model_json = {
					'url' : url,
					'model' : p.phone_model,
				}
				results.append(model_json)

	data = results
	if data:
		return JsonResponse(data,safe=False)		
	else:
		return JsonResponse('none', safe=False)
