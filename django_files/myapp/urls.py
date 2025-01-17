from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyModelViewSet
from . import views

router = DefaultRouter()
router.register(r'mymodels', MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('users/delete-all/', views.delete_all_users, name='delete-all-users'),
]
