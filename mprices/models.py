from django.db import models
from django.template.defaultfilters import slugify
from datetime import date
from django.urls import reverse

class Country(models.Model):
	country = models.CharField(max_length=75, unique=True)
	country_slug = models.CharField(max_length=75, blank=True, editable=False)
	currency = models.CharField(max_length=5, blank=True)
	exchange_rate = models.DecimalField(blank=True, default=0, decimal_places=6, max_digits=12)

	def __str__(self):
		return self.country.title()

	def save(self, *args, **kwargs):
		self.country = self.country.title()
		self.country_slug = slugify(self.country)
		self.currency = self.currency.upper()
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['country']
		verbose_name_plural = 'Countries'


class Location(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, related_name='cities')
	location_name = models.CharField(max_length=50, unique=True)
	location_slug = models.CharField(max_length=50, blank=True, editable=False)

	def __str__(self):
		return self.location_name.title()

	def save(self, *args, **kwargs):
		self.location_name = self.location_name.lower()
		self.location_slug = slugify(self.location_name)
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['location_name']
		verbose_name_plural = 'Locations'


class Brand(models.Model):
	brand_name = models.CharField(max_length=75, unique=True)
	brand_slug = models.CharField(max_length=75, blank=True, editable=False)

	def __str__(self):
		return self.brand_name.title()

	def save(self, *args, **kwargs):
		self.brand_name = self.brand_name.lower()
		self.brand_slug = slugify(self.brand_name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('brand', args=[str(self.brand_slug),])

	class Meta:
		ordering = ['brand_name']
		verbose_name_plural = 'Brands'


class Phone(models.Model):
	brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='phones')
	phone_model = models.CharField(max_length=100, unique=True)
	price = models.IntegerField(blank=True, default=0)
	gsm_arena = models.CharField(max_length=255, blank=True)
	release = models.DateField(default=date.today)
	phone_model_slug = models.CharField(max_length=100, blank=True, editable=False)
	phone_image = models.ImageField(upload_to='uploads/images', blank=True)	

	#Specifications
	description = models.TextField(blank=True)

	#Build
	os = models.CharField(max_length=100, blank=True)
	dimensions = models.CharField(max_length=100, blank=True)
	weight = models.CharField(max_length=50, blank=True)	
	sim = models.CharField(max_length=100, blank=True)
	colors = models.CharField(max_length=100, blank=True)

	#Processor
	cpu = models.CharField(max_length=200, blank=True)
	chipset = models.CharField(max_length=100, blank=True)
	gpu = models.CharField(max_length=100, blank=True)

	#Display
	technology = models.CharField(max_length=100, blank=True)
	size = models.CharField(max_length=100, blank=True)
	resolution = models.CharField(max_length=100, blank=True)
	protection = models.CharField(max_length=100, blank=True)

	#Memory
	builtin = models.CharField(max_length=100, blank=True)
	card = models.CharField(max_length=100, blank=True)

	#Camera
	main_camera = models.CharField(max_length=100, blank=True)
	features = models.CharField(max_length=250, blank=True)
	front_camera = models.CharField(max_length=250, blank=True)

	#Features
	sensors = models.CharField(max_length=250, blank=True)

	#Battery
	battery = models.CharField(max_length=100, blank=True)


	def __str__(self):
		return self.phone_model.title()

	def save(self, *args, **kwargs):
		self.phone_model = self.phone_model.lower()
		self.phone_model_slug = slugify(self.phone_model)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('phone', args=[str(self.phone_model_slug),])

	class Meta:
		ordering = ['-release', '-price']
		verbose_name_plural = 'Phones'




###############################################################################################################



