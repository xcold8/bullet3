from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^task/', views.taskfeed, name='taskfeed'),
	url(r'^login/', views.login, name='login'),
	url(r'^newtask/', views.newtask, name='newtask'),
]