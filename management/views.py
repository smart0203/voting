from datetime import date

from rest_framework import viewsets, status, generics
from rest_framework.response import Response

from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    
    def create(self, request):
        old_menu_count = Menu.objects.filter(restaurant=request.data["restaurant"], created_dt__date=date.today()).count()
        serializer = MenuSerializer(data=request.data)
        if old_menu_count == 0:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class VoteCreate(generics.ListCreateAPIView):
    serializer_class = VoteSerializer
    queryset = Vote.objects.all()

    def create(self, request):
        vote_count = Vote.objects.filter(employee=request.data["employee"], menu=request.data["menu"]).count()
        serializer = VoteSerializer(data=request.data)
        if vote_count < 3:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CurrentDayMenusList(generics.ListAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter(created_dt__date=date.today())
