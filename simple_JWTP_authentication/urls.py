from django.contrib import admin

from Api import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

routers=DefaultRouter()
routers.register('Studentapi',views.modelviewsets,basename='student')
# this is my frist change into this repo
#This is my second change in repo by manjeet singh

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(routers.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='token_verify'),
]