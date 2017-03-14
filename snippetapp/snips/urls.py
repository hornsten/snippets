from django.conf.urls import url
from snips import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<snip_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add/$', views.add, name="add"),
    url(r'^delete_snip/(?P<pk>\d+)$', views.delete_snip, name="delete_snip"),
    url(r'^snip/(?P<pk>[0-9]+)/$', views.SnipUpdate.as_view(), name="update_snip")
]
