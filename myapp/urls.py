from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('myendpoint',views.ProductView )

urlpatterns = [
    # url(r'^$', views.home),
    url(r'', include(router.urls)),
    url(r'^another/', views.another),
]