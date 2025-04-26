from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about', views.about, name='about'),  # About page
    path('services', views.services, name='services'),  # Services page
    path('contact', views.contact, name='contact'),  # Contact page
    path('aboutus', views.aboutus, name='aboutus'),  # Redirect to external site
    path('specialoffers', views.specialoffers, name='specialoffers'),  # Special offers page
    path('combo', views.combo, name='combo'),  # Combo page
    path('offer', views.offer, name='offer'),  # Offer page
]