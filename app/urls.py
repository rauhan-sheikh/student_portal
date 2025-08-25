from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, StaffViewSet, StudentViewSet, CourseViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
