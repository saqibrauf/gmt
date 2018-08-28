from django.urls import path
from . import views
from django.contrib.sitemaps import views as sm_views
from .sitemaps import BrandSitemap, PhoneSitemap

sitemaps = {
    'brands' : BrandSitemap(),
    'phones' : PhoneSitemap(),
}

urlpatterns = [
	#Sitemap
	path('sitemap.xml/', sm_views.index, {'sitemaps' : sitemaps }, name='django.contrib.sitemaps.views.sitemap'),
	path('sitemap-<section>.xml/', sm_views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('', views.index, name='index'),
    path('coming-soon', views.coming_soon, name='coming_soon'),
    path('<slug>-mobile-prices-in-<location>/', views.brand, name='brand'),
    path('<slug>-price-in-<location>/', views.phone, name='phone')
]