from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
from .models import Review
from users.models import User
from .serializers import ReviewSerializer

class ReviewList(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class UserView(APIView):
    pass

class CustomTokenObtainPairView(TokenObtainPairView):
    pass
    
class UserProfileView(APIView):
    pass
