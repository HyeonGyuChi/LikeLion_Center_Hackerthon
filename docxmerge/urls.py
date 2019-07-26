"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'docxmerge'
urlpatterns = [
    path('resume_upload/', views.resume_upload, name="upload"),
    path('resume_make/', views.resume_make, name="make"),
    path('resume_result/<int:pk>', views.resume_result, name="result"),
    path('resume_result/<int:pk>/<str:order_by>/<str:order_updown>', views.resume_result, name="result"),
    path('resume_detail/<int:pk>', views.resume_detail, name="detail"),
    path('resume_download/<int:pk>/<str:type>', views.resume_download, name="download"),
    path('resume_like/', views.resume_like, name='like'),
]
