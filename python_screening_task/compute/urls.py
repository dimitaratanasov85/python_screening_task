from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from compute import views

urlpatterns = [
    path('compute/', views.compute, name='compute'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
