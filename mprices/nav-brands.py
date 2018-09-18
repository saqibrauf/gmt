from .models import Brand

def brands(context):
	brands = Brand.objects.all().order_by('brand_name')
	return {'nav_brands': brands}