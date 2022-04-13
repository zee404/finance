"""finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from finance import views, settings

urlpatterns = [
    path('', views.index, name="dashboard"),
    path('users/', views.users_view, name="users"),
    path('createuser/', views.create_user, name="createuser"),
    path('userdetail/', views.user_detailview, name="userdetail"),
    path('roles/', views.roles_view, name="rolesview"),
    path('createrole/', views.create_role, name="create_role"),
    path('cmspages/', views.cmspages_view, name="cmspages_view"),
    path('cmsfaqview/', views.cmsfaq_view, name="cmsfaq_view"),
    path('blogpostview/', views.blogpost_view, name="blogpost_view"),
    path('announcementview/', views.announcement_view, name="announcement_vew"),
    path('newsletterview/', views.newsletter_view, name="newsletterview"),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
