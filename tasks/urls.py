from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = 'tasks'

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/like/', TaskViewSet.as_view(actions={'patch': 'like'}), name='like-action')
]
