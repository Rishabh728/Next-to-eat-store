from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import  *
from accounts import views

urlpatterns = [

    path('registerLogin/', views.register_or_login, name='registerLogin'),
    path('logout/', logout_view, name='logout'),

 
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)