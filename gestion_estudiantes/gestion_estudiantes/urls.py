from django.contrib import admin
from django.urls import path, include  # 👈 include es clave

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('estudiantes.urls')),  # 👈 conecta tu app
]