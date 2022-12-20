from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"restaurant", views.RestaurantViewSet, "restaurant")
router.register(r"menu", views.MenuViewSet, "menu")
router.register(r"employee", views.EmployeeViewSet, "employee")
router.register(r"vote", views.VoteViewSet, "vote")

urlpatterns = [
    path("", include(router.urls))
]