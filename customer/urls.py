from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="customer/index.html"), name="index"),
    path('customer1/', views.customer1, name="customer1"),
    path('customer2/', views.customer2, name="customer2"),
    path('customer3/', views.customer3, name="customer3"),
    path('customer4/', views.customer4, name="customer4"),
]
