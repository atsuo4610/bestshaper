from django.conf.urls import url
from . import views

from rest_framework import routers
from .views import UserViewSet, BrassiereViewSet

urlpatterns = [
    url(r'^$', views.index, name='index',),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_up_done/$', views.sign_up_done, name='sign_up_done'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
]


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entries', BrassiereViewSet)