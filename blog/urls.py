from django.urls import path
from . import views

# (. ka matlab h ki, blog ka views,agar kisi dusre app se views import karte to uska naam likhna padta)

urlpatterns = [
    path('',views.all_blogs, name='all blogs'),
]