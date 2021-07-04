from django.db import models
# Create your models here.
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=255, blank= True, null= True)
    customer_address = models.CharField(max_length=255, blank= True, null= True)
    meter_number = models.CharField(max_length=255, blank= True, null= True)
    day_rate1 = models.IntegerField(blank= True, null= True)
    day_rate2 = models.IntegerField(blank= True, null= True)
    night_rate1 = models.IntegerField(blank= True, null= True)
    night_rate2= models.IntegerField(blank= True, null= True)
    weekend_rate1 = models.IntegerField(blank= True, null= True)
    weekend_rate2 = models.IntegerField(blank= True, null= True)
    weekend_day_rate1 = models.IntegerField(blank= True, null= True)
    weekend_day_rate2 = models.IntegerField(blank= True, null= True)
    ec_day_rate = models.IntegerField(blank= True, null= True)
    ec_night_rate = models.IntegerField(blank= True, null= True)
    ec_weekend_day_rate = models.IntegerField(blank= True, null= True)
    ec_weekend_rate = models.IntegerField(blank= True, null= True)
    cost_day_rate = models.IntegerField(blank= True, null= True)
    cost_night_rate = models.IntegerField(blank= True, null= True)
    cost_weekend_day_rate = models.IntegerField(blank= True, null= True)
    cost_weekend_rate = models.IntegerField(blank= True, null= True)
    total_cost = models.IntegerField(blank= True, null= True)

    def __str__(self):
        return self.customer_name
    
    

