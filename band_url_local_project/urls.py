from django.conf.urls import url, include
from django.contrib import admin
from band_url_local.views import get_index
from accounts import urls as accounts_urls
from products import urls as products_urls
from payments import urls as payments_urls
from band_url_local import urls as band_urls
from django.views import static
from settings import MEDIA_ROOT
from band_url_local import views as band_views

urlpatterns = [
    url(r'^admin/', (admin.site.urls)),
    url(r'^products/', include(products_urls)),
    url(r'^payments/', include(payments_urls)),
    url(r'', include(band_urls)),
    url(r'^$', get_index, name='index'),

    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'', include(accounts_urls)),
    url(r'^merchandise/', band_views.get_merchandise, name='merchandise')


]
