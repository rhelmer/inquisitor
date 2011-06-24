from django.conf.urls.defaults import *


urlpatterns = patterns('products.views',
    url(r'^products/?$', 'index', name='products.index'),
    url(r'^products/(.*)$', 'product', name='products.product'),
)