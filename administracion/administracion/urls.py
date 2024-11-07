"""
URL configuration for administracion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

from coreadmin import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Sistema de Gestión Clinica SePrice'
admin.site.site_title = 'Clinica SePrice'
admin.site.index_title = 'Panel de Control'


urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home_view, name=''),
    path('', include('coreadmin.urls')),
    # path('logout/', auth_views.LogoutView.as_view(template_name='appointments/account/logout.html'),name='logout'),
]


# Retrieve images from /media/
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)