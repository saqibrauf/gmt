from django.contrib.sitemaps import Sitemap
from .models import Location, Brand, Phone

class BrandSitemap(Sitemap):

	def items(self):
		brands = Brand.objects.all()
		location = Location.objects.all()
		urls = list()
		for b in brands:
			for l in location:
				url = '/' + b.brand_slug + '-mobile-prices-in-' + l.location_slug + '/'
				urls.append(url)
		return urls

	changefreq = "daily"
	priority = 0.5

	def location(self, item):
		return item

class PhoneSitemap(Sitemap):

	def items(self):
		phones = Phone.objects.all()
		location = Location.objects.all()
		urls = list()
		for p in phones:
			for l in location:
				url = '/' + p.phone_model_slug + '-price-in-' + l.location_slug + '/'
				urls.append(url)
		return urls

	changefreq = "daily"
	priority = 0.5

	def location(self, item):
		return item