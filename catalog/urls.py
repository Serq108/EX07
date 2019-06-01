from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cars/$', views.CarListView.as_view(), name='cars'),
    url(r'^car/(?P<pk>\d+)$', views.CarDetailView.as_view(), name='car-detail'),
]
