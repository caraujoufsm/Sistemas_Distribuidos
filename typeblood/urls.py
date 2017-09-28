from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.cad_list, name='cad_list'),
]