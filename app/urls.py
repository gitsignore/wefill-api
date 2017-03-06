from django.conf.urls import url
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users', UserViewSet, "users")


urlpatterns = [
    url(r'^users/login/$', LoginView.as_view()),
]

urlpatterns += router.urls
