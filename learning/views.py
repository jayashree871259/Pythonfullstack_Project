from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Lesson, Enrollment

def home_view(request):
    courses = Course.objects.filter(is_published=True)
    return render(request, 'home.html', {'courses': courses})

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            User.objects.create_user(username=username, password=password, email=email)
            messages.success(request, 'Account created! Please login')
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    enrolled_ids = enrollments.values_list('course__id', flat=True)
    all_courses = Course.objects.filter(is_published=True)
    available_courses = all_courses.exclude(id__in=enrolled_ids)
    return render(request, 'dashboard.html', {
        'enrollments': enrollments,
        'my_courses': [e.course for e in enrollments],
        'available_courses': available_courses,
        'courses': all_courses,
    })

@login_required
def enroll_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    Enrollment.objects.get_or_create(student=request.user, course=course)
    return redirect('dashboard')

@login_required
def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all().order_by('order')
    is_enrolled = Enrollment.objects.filter(student=request.user, course=course).exists()
    return render(request, 'course_detail.html', {
        'course': course,
        'lessons': lessons,
        'is_enrolled': is_enrolled,
    })
def courses_view(request):
    courses = Course.objects.filter(is_published=True)
    enrolled_ids = []
    if request.user.is_authenticated:
        enrolled_ids = list(Enrollment.objects.filter(student=request.user).values_list('course__id', flat=True))
    return render(request, 'courses.html', {'courses': courses, 'enrolled_ids': enrolled_ids})