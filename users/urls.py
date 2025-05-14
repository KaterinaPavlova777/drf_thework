from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import PaymentsViewSet, UserCreateAPIView, PaymentsCreateAPIView

app_name = UsersConfig.name

router = SimpleRouter()
router.register("", PaymentsViewSet)

urlpatterns = [
    path("login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "token/refresh",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path(
        "register/",
        UserCreateAPIView.as_view(permission_classes=(AllowAny,)),
        name="register",
    ),
    path("payment/", PaymentsCreateAPIView.as_view(), name="payment_create"),
]
