from django.urls import path
from account import views

urlpatterns = [
    path('', views.Welcome.as_view(), name='welcome_page'),
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('logout/', views.LogoutView.as_view(), name='logout_page'),
    path('forget_password/', views.ForgetPasswordView.as_view(), name='forget_pass_page'),
    path('forget_password/<email>', views.ResetPasswordView.as_view(), name='reset_pass_page'),
]
