from django.conf.urls import include, url
from django.contrib import admin
from app import views as views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^task/', views.taskfeed, name='taskfeed'),
    url(r'^login$', views.login, name='login'),
    url(r'^newtask$', views.newtask, name='newtask'),
]
