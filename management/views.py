from datetime import date

from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer


class RestaurantViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class MenuViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
    def create(self, request):
        old_menu_count = Menu.objects.filter(
            restaurant=request.data["restaurant"],
            employee=request.user.id,
            created_dt__date=date.today()).count()
        serializer = MenuSerializer(data=request.data)
        if old_menu_count == 0:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class VoteCreate(LoginRequiredMixin, generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def create(self, request):
        vote_count = Vote.objects.filter(
            employee=request.data["employee"],
            menu=request.data["menu"],
            created_dt__date=date.today()).count()
        serializer = VoteSerializer(data=request.data)
        if vote_count < 3:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CurrentDayMenusList(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter(created_dt__date=date.today())


class CurrentDayResult(LoginRequiredMixin, generics.ListAPIView):
    serializer_class = VoteSerializer
    
    def list(self):
        response = Vote.objects\
            .filter(created_dt__date=date.today())\
            .values('menu')\
            .annotate(count=Count('menu'))\
            .values("menu__restaurant__name", "count")\
            .order_by("count")
        return Response(response, status=status.HTTP_201_CREATED)