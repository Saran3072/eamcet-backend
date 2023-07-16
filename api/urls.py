from django.contrib import admin
from django.urls import path, include
from api import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', views.home, name='index'),
    path('https://eamcet-backend.onrender.com', TemplateView.as_view(template_name = 'index.html')),
    path('<slug:id>', views.pred),
]
