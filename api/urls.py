from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

router = routers.DefaultRouter()


router.register('niveau', NiveauViewSet)
router.register('employee', EmployeeViewSet)
router.register('presence', PresenceViewSet)
router.register('conge', CongeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view())
]