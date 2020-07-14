from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^email/$',views.email,name = 'email'),
    url(r'^create_profile/$',views.create_profile,name = 'create_profile'),
    url(r'^profile/(?P<profile_id>\d+)',views.profile,name = 'profile'),
    url(r'^project/(?P<project_id>\d+)',views.project,name = 'project'),
    url(r'^add_project/$',views.add_project,name = 'add_project'),
    url(r'^rate_project/(?P<project_id>\d+)',views.rate_project,name = 'rate_project'),
    url(r'^search_project/$',views.search_project,name = 'search_project'),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
]