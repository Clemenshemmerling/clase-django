from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.product_view, name='product'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail),
	url(r'^product_new', views.new_product, name='new_product ')
]

