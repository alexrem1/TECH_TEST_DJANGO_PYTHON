from .models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    customer_name = forms.CharField(required=False, max_length=255, 
    widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Customer Name", "name": "customer_name"}
    ))
    
    customer_address = forms.CharField(required=False, max_length=5, 
    widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Number Of Pages"}
    ))

    meter_number = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))

    day_rate1 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    weekend_day_rate1 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    night_rate1 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    weekend_rate1 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    day_rate2 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    weekend_day_rate2 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    night_rate2 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    weekend_rate2 = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    ec_day_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    ec_weekend_day_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    ec_night_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    ec_weekend_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    cost_day_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    cost_weekend_day_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    cost_night_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   
    cost_weekend_rate = forms.DecimalField(required=False, max_digits=6, decimal_places=2, 
    widget=forms.NumberInput(
        attrs={"class": "form-control", "placeholder": "Price"}
    ))   

    class Meta:
        model= Customer
        fields = "__all__"