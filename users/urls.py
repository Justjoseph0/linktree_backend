from django.urls import path
from .views import CreateUserAPIView,LoginView,ProfileApiView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='users'),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileApiView.as_view(), name='profile'),
]