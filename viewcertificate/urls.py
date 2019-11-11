from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.view_certificate, name='BIB_NO'),
    url(r'^result/$', views.bib_no_submission, name='result'),
]