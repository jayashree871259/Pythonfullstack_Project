from django.urls import path
from learning import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('courses/', views.courses_view, name='courses'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('enroll/<int:course_id>/', views.enroll_view, name='enroll'),
    path('course/<int:course_id>/', views.course_detail_view, name='course_detail'),
]
