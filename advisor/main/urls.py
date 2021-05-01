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

    path('admin/advisor/',views.AdvisorApi.as_view()),
    path('user/advisor/', views.AdvisorApi.as_view()),
    # path('user/advisor/<int:pk>/', views.AdvisorApi.as_view()),

    path('user/<int:user_id>/advisor/<int:advisor_id>/', views.BookingApi.as_view()),
    path('user/<int:user_id>/advisor/booking/', views.BookingApi.as_view()),
]