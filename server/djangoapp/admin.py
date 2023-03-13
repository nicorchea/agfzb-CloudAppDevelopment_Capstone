from django.contrib import admin
# from .models import related models


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline

# Register models here
from .models import CarMake, CarModel

class CarModelInline(admin.TabularInline):
    model = CarModel

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'car_type', 'year', 'dealer_id')
    list_filter = ('make', 'car_type', 'year')
    search_fields = ('name', 'make__name')

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
