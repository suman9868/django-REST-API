
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employees/$', views.employeesList.as_view()),
    url(r'^employees/(?P<pk>[0-9]+)/$', views.employeesDetail.as_view()),
]
