from mprices.models import Brand, Country, Location
from django.contrib.gis.geoip2 import GeoIP2

def global_var(request):
	all_brands = Brand.objects.all().order_by('brand_name')
	countries = Country.objects.all()
	return {
		'all_brands' : all_brands,
		'countries' : countries,
	}


def USER_LOCATION(request):

	if request.method == 'POST':
		COUNTRY = request.POST['country']
		if COUNTRY != 'global':
			try:
				country = Country.objects.get(country_slug__iexact=COUNTRY)
				base_cur = Country.objects.get(currency='USD')
				base = 1 / base_cur.exchange_rate
				er = country.exchange_rate
				exch = base * er
				request.session['currency'] = country.currency
				request.session['exchange'] = float(exch)
			except:
				request.session['currency'] = 'USD'
				request.session['exchange'] = 1
		else:
			request.session['currency'] = 'USD'
			request.session['exchange'] = 1
		request.session['country'] = COUNTRY.replace('-', ' ')
		request.session['city'] = ''

	elif 'country' not in request.session:
		g = GeoIP2()
		ip = request.META.get('REMOTE_ADDR', None)
		if ip == '127.0.0.1':
			ip = 'getmobileprice.com'
		CITY = g.city(ip)['city']
		COUNTRY = g.country(ip)['country_name']
		try:
			country = Country.objects.get(country__iexact=COUNTRY)
			base_cur = Country.objects.get(currency='USD')
			base = 1 / base_cur.exchange_rate
			er = country.exchange_rate
			exch = base * er
			request.session['currency'] = country.currency
			request.session['exchange'] = float(exch)
		except:
			request.session['currency'] = 'USD'
			request.session['exchange'] = 1
		request.session['country'] = COUNTRY
		request.session['city'] = CITY

	elif request.session['country']:
		COUNTRY = request.session['country']
		try:
			country = Country.objects.get(country__iexact=COUNTRY)
			base_cur = Country.objects.get(currency='USD')
			base = 1 / base_cur.exchange_rate
			er = country.exchange_rate
			exch = base * er
			request.session['currency'] = country.currency
			request.session['exchange'] = float(exch)
		except:
			request.session['currency'] = 'USD'
			request.session['exchange'] = 1
		request.session['country'] = COUNTRY

	return {}