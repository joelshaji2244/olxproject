"""
URL configuration for olxapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from olx.views import OlxCreateView,OlxListView,OlxDeleteView,OlxDetailView,OlxUpdateView,RegistrationView,LoginView,logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration', RegistrationView.as_view(), name="olx-reg"),
    path('login', LoginView.as_view(), name="olx-login"),
    path('logout', logout_view, name="olx-logout"),
    path('olx/add', OlxCreateView.as_view(), name="olx-add"),
    path('olx/list', OlxListView.as_view(), name="olx-list"),
    path('olx/<int:pk>', OlxDetailView.as_view(), name="olx-detail"),
    path('olx/<int:pk>/remove', OlxDeleteView.as_view(), name="olx-delete"),
    path('olx/<int:pk>/edit', OlxUpdateView.as_view(), name="olx-edit"),
    path('v1/olx/', include("vechiles.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
