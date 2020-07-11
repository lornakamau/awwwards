from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^project/$',views.project,name = 'project'),
]