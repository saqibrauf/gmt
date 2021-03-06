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
				request.session['city'] = ''
			except:
				request.session['currency'] = 'USD'
				request.session['exchange'] = 1
				request.session['city'] = ''
		else:
			request.session['currency'] = 'USD'
			request.session['exchange'] = 1
			request.session['city'] = ''
		request.session['country'] = COUNTRY.replace('-', ' ')

	elif 'country' not in request.session:
		g = GeoIP2()
		ip = request.META.get('HTTP_X_REAL_IP', None)#This is to retrieve Client IP on PythonAnywhere
		try:
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
		except:
			request.session['country'] = 'global'
			request.session['currency'] = 'USD'
			request.session['exchange'] = 1

	elif request.session['country']:
		COUNTRY = request.session['country']
		if COUNTRY != 'global':
			try:
				country = Country.objects.get(country__iexact=COUNTRY)
				base_cur = Country.objects.get(currency='USD')
				base = 1 / base_cur.exchange_rate
				er = country.exchange_rate
				exch = base * er
				request.session['currency'] = country.currency
				request.session['exchange'] = float(exch)
				request.session['country'] = COUNTRY
			except:
				request.session['currency'] = 'USD'
				request.session['exchange'] = 1

		else:
			request.session['country'] = 'global'
			request.session['currency'] = 'USD'
			request.session['exchange'] = 1

	else:
		request.session['country'] = 'global'
		request.session['currency'] = 'USD'
		request.session['exchange'] = 1

	return {}