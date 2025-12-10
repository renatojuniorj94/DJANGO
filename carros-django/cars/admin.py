from django.contrib import admin
from cars.models import car

# Register your models here.
class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model',)

admin.site.register(car, carAdmin)