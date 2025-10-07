from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
def user_register(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def profile_edit(request):
    return render(request, 'profile.html')

def user_notes(request):
    return render(request, 'notes.html')

def edit_note(request):
    return render(request, 'edit_note.html')
