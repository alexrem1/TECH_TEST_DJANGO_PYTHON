from django.contrib import admin
from .models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "customer_address",
        "meter_number",
        "day_rate1",
        "day_rate2",
        "night_rate1",
        "night_rate2",
        "weekend_day_rate1",
        "weekend_day_rate2",
        "weekend_rate1",
        "weekend_rate2", 
        "ec_day_rate",
        "ec_weekend_rate",
        "ec_night_rate",
        "ec_weekend_day_rate",
        "cost_day_rate",
        "cost_night_rate",
        "cost_weekend_rate",
        "cost_weekend_day_rate",
        "total_cost"
    )

admin.site.register(Customer, CustomerAdmin)
