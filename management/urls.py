from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"restaurant", views.RestaurantViewSet, "restaurant")
router.register(r"menu", views.MenuViewSet, "menu")
router.register(r"employee", views.EmployeeViewSet, "employee")

urlpatterns = [
    path("", include(router.urls)),
    path("vote/", views.VoteCreate.as_view()),
    path("get_currentday_menu/", views.CurrentDayMenusList.as_view()),
    path("get_currentday_result/", views.CurrentDayResult.as_view())
]