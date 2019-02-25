from django.urls import path
from . import views
from django.contrib.sitemaps import views as sm_views
from django.views.generic import TemplateView
from .sitemaps import BrandSitemap, PhoneSitemap, BrandSimple, PhoneSimple

sitemaps = {
    'brands' : BrandSitemap(),
    'phones' : PhoneSitemap(),
    'brands-s' : BrandSimple(),
    'phone-s' : PhoneSimple(),
}

urlpatterns = [
	#Sitemap
	path('sitemap-index.xml/', sm_views.index, {'sitemaps' : sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
	path('sitemap-<section>.xml/', sm_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	#General
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<slug>-mobile-prices/', views.brand, name='brand'),
    path('<slug>-mobile-prices-in-<location>/', views.brand, name='brand'),
    path('<slug>-price/', views.phone, name='phone'),
    path('<slug>-price-in-<location>/', views.phone, name='phone'),
    #AJAX Phone Search
    path('get_phone/', views.get_phone, name='get_phone'),
    #Robot
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt'), name="robot"),
]