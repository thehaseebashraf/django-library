from django.contrib import admin
from django.urls import path, include # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("books.urls")), 
    path("api/", include("apis.urls")),  # new
]
