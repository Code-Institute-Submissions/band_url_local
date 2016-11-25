from django.conf.urls import url
from .views import make_payment, buy_now

urlpatterns = [
    url(r'^stripe/', make_payment, name='make_payment_stripe'),
    url(r'^buy_now/(?P<id>\d+)', buy_now, name='buy_now_stripe'),
]