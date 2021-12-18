from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name = 'home'),
	path('portofolio/', views.portofolio, name = 'portofolio'),
	path('contact/', views.contact, name = 'contact'),
	path('a-propos/', views.about, name = 'about'),
]