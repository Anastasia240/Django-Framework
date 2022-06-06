from django.conf import settings

from authapp.apps import AuthappConfig
from django.urls import path, include
from authapp.views import CustomLoginView, RegisterView, CustomLogoutView, EditView
from django.contrib import admin
app_name = AuthappConfig.name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit/', EditView.as_view(), name='edit'),
    path('social_auth/', include('social_django.urls', namespace='social'))

]








