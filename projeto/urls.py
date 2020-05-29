"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views #componente principal 
from django.urls import path

from courses import views as views_courses
#settings
from django.conf import settings
from django.conf.urls.static import static


home = views.home #rota home dentro do core/views.py
contacts = views.contacts






urlpatterns = [
    path('', home , name='home'), #para urls vazias
    path('teste', views.teste , name='teste'),
    path('contacts/', contacts, name='contacts'),
    path('admin/', admin.site.urls),
    path('courses/', views_courses.courses, name='courses'), #o name ficará disponivel no {% url name %}
    path('courses/<int:id>/', views_courses.details, name='details')
]           #qualquer valor inteiro irá ser inserido courses/?pk=1
            #substituiu o (?p<pk>\d+)

#pegando as urls das imagens e acrescentando na rota
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)