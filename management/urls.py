from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"restaurant", views.RestaurantViewSet, "restaurant")
router.register(r"menu", views.MenuViewSet, "menu")

urlpatterns = [
    path("", include(router.urls))
]

# urlpatterns = format_suffix_patterns(urlpatterns)