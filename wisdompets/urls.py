from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from adoptions import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('^$', views.home, name='home'),
    url('^adoptions/(\d+)/', views.pet_detail, name='pet_detail'),
]
