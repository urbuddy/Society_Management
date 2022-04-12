from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'sc'
urlpatterns = [
    path('', views.home, name='home'),
    path('add_notice/',views.add_notice, name='add_notice'),
    path('add_complaint/', views.add_complaint, name='add_complaint'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('profile/', views.profile, name='profile'),

    path('signup/', views.signup, name='signup'),
    path('otp/', views.otp_verify, name='otp'),
    path('login/', views.Login, name='login'),
    path("logout/", views.Logout, name='logout'),

    # Reset The Password
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='sc/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='sc/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='sc/password_reset_complete.html'), name="password_reset_complete")

]
