from django.contrib import admin
from django.urls import path
from django.urls import include
from search import views as search_views
from users import views as login_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search_views.search, name='search'),
    path('login/', login_views.login, name='login'),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
]
