from django.conf.urls import url
from payments.views import make_payment, buy_now
from accounts.views import register, profile, logout, login
import views


urlpatterns = [
    url(r'^blog/$', views.post_list, name='blog'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<id>\d+)/edit$', views.edit_post),



]
