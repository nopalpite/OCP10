from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer

class SignupView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
