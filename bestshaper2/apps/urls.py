from django.conf.urls import url
from . import views, api

# from rest_framework import routers
from .views import UserViewSet, BrassiereViewSet

urlpatterns = [
    url(r'^$', views.index, name='index',),
    url(r'^sign_up/$', views.sign_up, name='sign_up'),
    url(r'^sign_up_done/$', views.sign_up_done, name='sign_up_done'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^bra_admin/$', views.bra_admin, name='bra_admin'),
    url(r'^api/hoge$', api.post_wash_num, name='post_wash'),

    #ブラジャーごとの情報の書き込み
    # url(r'^bra_admin/$', views.bra_admin, name='bra_admin'),
    # url(r'^api/bra_data$', views.bra_data, name='bra_admin'),

]

#
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'brassieres', BrassiereViewSet)