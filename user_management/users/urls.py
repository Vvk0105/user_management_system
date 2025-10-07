from django.urls import path
from .views import RegisterView, ProfileView,user_register,login_page,profile_edit,user_notes,edit_note, reset_password,ResetPasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('user_register/', user_register, name='user_register'),
    path('', login_page, name='login_page'),
    path('edit-profile/', profile_edit, name='edit_profile'),
    path('user-notes/', user_notes, name='user_notes'),
    path('edit-note/', edit_note, name='edit_note'),
    path('reset-password/', reset_password, name='reset_password'),
    path('api/reset-password/', ResetPasswordView.as_view(), name='api_reset_password'),


]