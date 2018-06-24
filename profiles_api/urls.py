from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile',views.UserProfileViewSet) #En caso de model view set no necesita el base_name
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),
]


# "token": "4ba39113fb56d0a2e2633fa46b192dd71dc35673"
