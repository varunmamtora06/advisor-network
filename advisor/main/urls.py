from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('', views.index, name='index'),
    path('user/register/',views.RegisterNewUserView.as_view()),
    # path('api-newuser-login',views.LoginNewUserView.as_view()),
    
    path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]