from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from management import views

urlpatterns = [
    path('restaurant/', views.RestaurantList.as_view()),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)