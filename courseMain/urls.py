"""courseMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from courseMain import settings
import studCourse.views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', studCourse.views.index, name ='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^courses/$', studCourse.views.CourseListView.as_view(), name ='courses'),
    url(r'^courses/(?P<pk>\d+)$', studCourse.views.CourseDetailView, name='course-detail'),
    url('^tsturl/', studCourse.views.indextsturl),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)