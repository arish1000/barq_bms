from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from users.serializers import LoginSerializer


def login_view(request):
    if request.user.is_authenticated:
        next_url = request.GET.get("next", "/admin/")

        return redirect(next_url)
    
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                next_url = request.GET.get("next", "/admin/")

                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, "users/login.html")


@api_view(['POST'])
@permission_classes([AllowAny])
def token_login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        context = {
            'token': token.key,
            'user_id': user.id,
            'username': user.username
        }
        return Response(context, status=HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

def logout_view(request):
    logout(request)

    return redirect("login")
