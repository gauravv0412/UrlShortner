from django.urls import path

from main import views

urlpatterns = [
    path('<str:url>', views.fetch),
    path('', views.get_url)
]