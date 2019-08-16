from django.urls import path, include

from main import views

urlpatterns = [
    path('auth/', include('auth.urls')),
    path('<str:url>', views.fetch),
    path('', views.get_url)
]