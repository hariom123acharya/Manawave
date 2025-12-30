from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),   # login: get access & refresh
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


    
]
