from django.contrib import admin
from django.urls import path
from django.urls import include
from search import views as search_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_views.search, name='search'),
    path('', include('km.urls')),
    path('about/', include('about.urls')),
]
