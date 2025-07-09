from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from loginapp.views import login_view

def home(request):
    return HttpResponse("¡Bienvenido a la página principal!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('', home),  # ruta raíz
]
