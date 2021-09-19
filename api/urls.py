from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, ProjectViewSet, CreateUserView, ListUserView, LoginUserView, ProfileViewSet,CommentViewSet

router = routers.DefaultRouter()
router.register('project', ProjectViewSet)
router.register('tasks', TaskViewSet)
router.register('profile', ProfileViewSet)
router.register('comment', CommentViewSet)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls)),
]