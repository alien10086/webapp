from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^my_view/$', views.my_view, name= 'my_view'),
    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^sub_article/', views.sub_article, name='sub_article'),
    url(r'^homepage/$', views.homepage, name= 'homepage'),
    url(r'^add_register/', views.add_register, name= 'add_register'),
    url(r'^register/', views.register, name= 'register'),
    url(r'^logout/', views.logout_view, name= 'logout_view'),
    url(r'^(?P<entry_id>[0-9]+)/look/$', views.look, name= 'look'),
    url(r'^(?P<article_id>[0-9]+)/compile/$', views.compile, name='compile'),
    url(r'^(?P<article_id>[0-9]+)/edit/$', views.edit, name='edit'),




]
