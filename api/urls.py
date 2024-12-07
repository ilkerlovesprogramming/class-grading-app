from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_routes),
    path('students/', views.get_students),
    path('ongoing-courses/', views.get_ongoing_courses),
    path('student-details/', views.get_student_details),
    path('student-average-grade/', views.get_student_average_grade),
    path('student-ongoing-courses/', views.get_student_ongoing_courses),
    path('student-completed-courses/', views.get_student_completed_courses),
    path('student-course-grade/', views.get_student_course_grade),
]