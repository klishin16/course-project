from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('organizations', views.organizations, name='organizations'),
    path('organization', views.organizationInfo, name='organizationInfo'),
    path('orders', views.orders, name='orders'),
    path('order', views.orderInfo, name='orderInfo'),
    path('authentication', views.authentication, name='authentication'),
    path('auth', views.auth, name='auth'),
    path('addOrder', views.addOrder, name='addOrder'),
    path('addOrganization', views.addOrganization, name='addOrganization'),
    path('removeOrganization', views.removeOrganization, name='removeOrganization'),
    path('removeOrder', views.removeOrder, name='removeOrder')
]
