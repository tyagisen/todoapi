from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from todoapp.views import TodoViewSet

router = DefaultRouter()

router.register('todo', TodoViewSet, basename = 'Todo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
