from django.contrib import admin
from apps.products.models import MeasureUnit, CategoryProducts, Indicador, Product

# Register your models here.

admin.site.register(MeasureUnit)
admin.site.register(CategoryProducts)
admin.site.register(Indicador)
admin.site.register(Product)
