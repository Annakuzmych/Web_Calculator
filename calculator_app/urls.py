from django.urls import path
from . import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="Your API Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/',  views.redoc, name='redoc'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('calculator/', views.calculator, name='calculator'),
    path('number_converter/', views.number_converter, name='number_converter'),
    path('history_view/', views.history_view, name='history_view'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('clear_history/', views.clear_history, name='clear_history'),
    #path('login/', auth_views.LoginView.as_view(authentication_form=LoginForm), name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
