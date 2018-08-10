from django.urls import path, re_path
from mainApp.views import UserCreateAPIView, UserUpdateAPIView, UserGetEthAPIView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
	path('createUser/', UserCreateAPIView.as_view(), name='createUser'),
	path('login/', obtain_jwt_token, name='login'),
	re_path(r'^get_eth/(?P<pk>\d+)$', UserGetEthAPIView.as_view(), name='get_eth'),
	re_path(r'^set_eth/(?P<pk>\d+)$', UserUpdateAPIView.as_view(), name='set_eth'),
]