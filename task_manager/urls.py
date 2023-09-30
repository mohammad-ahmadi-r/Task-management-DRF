from django.contrib import admin
from django.urls import path, include
from tasks.views import Tasks
from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'tasks', Tasks, basename='tasks')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('users/', include('users.urls'))
]
