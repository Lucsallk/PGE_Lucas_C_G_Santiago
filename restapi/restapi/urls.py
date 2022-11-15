from django.contrib import admin
from django.urls import path
from restapi import views
# Need to check patch
urlpatterns = [
    path('admin/', admin.site.urls),
    path('estagiarios/', views.estagiarios_list),
    path('estagiarios/<int:id>', views.estagiarios_detail),
    path('setores/', views.setores_list),
    path('setores/<int:id>', views.setores_detail),
]
