from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^profile/$',views.profile,name = 'profile'),
    url(r'^project/$',views.project,name = 'project'),
    url(r'^add_project/$',views.add_project,name = 'add_project'),
    url(r'^rate_project/(?P<image_id>\d+)',views.rate_project,name = 'rate_project'),
    url(r'^search_project/(?P<image_id>\d+)',views.search_project,name = 'search_project'),
]