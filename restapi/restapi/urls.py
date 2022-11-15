from django.contrib import admin
from django.urls import path, include
from restapi import views
from rest_framework import routers
from .views import EstagiariosViewSet, SetoresViewSet
# Need to check patch

router = routers.DefaultRouter()
router.register(r'estagiarios', EstagiariosViewSet, basename = 'estagiarios')
router.register(r'setores', SetoresViewSet, basename = 'setores')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]