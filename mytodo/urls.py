
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('home page')

urlpatterns = [
    path('', home),
    path('mylist/', include('mylist.urls')),
    path('admin/', admin.site.urls),
]
