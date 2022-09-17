from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()


router.register('niveau', NiveauViewSet)
router.register('employee', EmployeeViewSet)
router.register('presence', PresenceViewSet)
router.register('conge', CongeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]