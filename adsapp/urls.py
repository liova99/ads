from django.conf.urls import url
from . import views

app_name = 'adsapp'

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name = 'index'),
    url(r'^register/$', views.UserFormView.as_view(), name = 'register'),
    url(r'^item/(?P<pk>[0-9]+)/$', views.DetailPageView.as_view(), name = 'detail'),
    url(r'^about/$', views.AboutPageView.as_view(), name = 'about'),
    url(r'^add_new_item/$', views.ArticleCreate.as_view(), name = 'add_new'),
    url(r'^update_item/(?P<pk>[0-9]+)/$', views.ArticleUpdate.as_view(), name = 'update_item'),
    url(r'^item/(?P<pk>[0-9]+)/delete/$', views.ArticleDelete.as_view(), name = 'delete_item'),

]