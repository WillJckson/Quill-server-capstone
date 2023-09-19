from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from Quillapi.views import register_user, login_user
from Quillapi.views import QuoteView
from django.contrib import admin
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'quotes', QuoteView, 'quote')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    # other URL patterns
    path('', include(router.urls)),
]
