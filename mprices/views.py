from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
from .models import Location, Brand, Phone, Country
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	phones = Phone.objects.filter(price__gt=0).order_by('-release', '-price')	

	page = request.GET.get('page', 1)
	paginator = Paginator(phones, 50)
	try:
		phones = paginator.page(page)
	except PageNotAnInteger:
		phones = paginator.page(1)
	except EmptyPage:
		phones = paginator.page(paginator.num_pages)	

	context = {
		'phones' : phones,
	}
	return render(request, 'mprices/index.html', context)


def search(request):
	if request.GET:
		min_price = request.GET.get('minprice', '100')
		max_price = request.GET.get('maxprice', '250')
		phones = Phone.objects.filter(price__gte=min_price, price__lte=max_price).order_by('-price')
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
		
		context = {
			'phones' : phones,
			'message' : message,
		}

	else:
		message = ''
		context = {
			'message' : message,
		}
	return render(request, 'mprices/search.html', context)


def brand(request, slug, location=''):
	brand = get_object_or_404(Brand, brand_slug=slug)
	phones = brand.phones.all().order_by('-release', '-price')

	if location:
		try:
			city = get_object_or_404(Location, location_slug=location)
			request.session['city'] = city.location_name
			request.session['city_slug'] = city.location_slug
			request.session['country'] = city.country.country
		except:
			request.session['city'] = ''
			request.session['city_slug'] = ''
			if 'country' not in request.session:
				request.session['country'] = 'global'
	else:
		request.session['city'] = ''
		request.session['city_slug'] = ''
		if 'country' not in request.session:
			request.session['country'] = 'global'

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
	}
	return render(request, 'mprices/brand.html', context)

def phone(request, slug, location=''):
	phone = get_object_or_404(Phone, phone_model_slug=slug)
	brand = phone.brand_name
	all_phones = Phone.objects.filter(brand_name=brand).exclude(id=phone.id).order_by('-release', '-price')

	if location:
		try:
			city = get_object_or_404(Location, location_slug=location)
			request.session['city'] = city.location_name
			request.session['city_slug'] = city.location_slug
			request.session['country'] = city.country.country
		except:
			request.session['city'] = ''
			request.session['city_slug'] = ''
			if 'country' not in request.session:
				request.session['country'] = 'global'
	else:
		request.session['city'] = ''
		request.session['city_slug'] = ''
		if 'country' not in request.session:
			request.session['country'] = 'global'

	context = {
		'phone' : phone,
		'brand' : brand,
		'all_phones' : all_phones,
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
