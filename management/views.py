from datetime import date

from django.db.models import Count
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import viewsets, status, generics, permissions, views
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Restaurant, Menu, Employee, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer,\
    VoteSerializer, LoginSerializer, SignupSerializer


class SignupView(generics.CreateAPIView):
    """
    Class Based View for Signup API
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignupSerializer


class LoginView(TokenObtainPairView):
    """
    Class Based View for Login API
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer


class LogoutView(views.APIView):
    """
    Class Based View for Logout API
    """
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class RestaurantViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    Class Based Viewset for Restaurant API
    """
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class MenuViewSet(LoginRequiredMixin, viewsets.ModelViewSet):
    """
    Class Based Viewset for Menu API
    """
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
    """
    Class Based Viewset for Employee API
    """
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class VoteCreate(LoginRequiredMixin, generics.ListCreateAPIView):
    """
    Class Based Viewset for Vote API
    """
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
    """
    Class Based APIView to Get Current Day Menus
    """
    serializer_class = MenuSerializer
    queryset = Menu.objects.filter(created_dt__date=date.today())


class CurrentDayResult(LoginRequiredMixin, generics.ListAPIView):
    """
    Class Based APIView to Get Current Day Result
    """
    serializer_class = VoteSerializer
    
    def list(self):
        response = Vote.objects\
            .filter(created_dt__date=date.today())\
            .values('menu')\
            .annotate(count=Count('menu'))\
            .values("menu__restaurant__name", "count")\
            .order_by("count")
        return Response(response, status=status.HTTP_201_CREATED)