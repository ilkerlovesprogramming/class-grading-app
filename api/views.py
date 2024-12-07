from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg
from .models import Student, OngoingCourse, CompletedCourse

@api_view(['GET'])
def api_routes(request):
    routes = [
        {'GET': '/api/students/'},
        {'GET': '/api/ongoing-courses/'},
        {'GET': '/api/student-details/'},
        {'GET': '/api/student-average-grade/'},
        {'GET': '/api/student-ongoing-courses/'},
        {'GET': '/api/student-completed-courses/'},
        {'GET': '/api/student-course-grade/'},
    ]
    return Response(routes)

@api_view(['GET'])
def get_students(request):
    try:
        students = Student.objects.all()
        return Response([{'id': student.id, 'name': student.name} for student in students])
    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def get_ongoing_courses(request):
    courses = OngoingCourse.objects.all()
    data = [{
        'id': course.id,
        'name': course.name,
        'department': course.department,
        'description': course.description,
        'remaining_seats': course.remaining_seats
    } for course in courses]
    return Response(data)

@api_view(['GET'])
def get_student_details(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(id=student_id)
        data = {
            'id': student.id,
            'name': student.name,
            'department': student.department,
            'semester': student.semester
        }
        return Response(data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

@api_view(['GET'])
def get_student_average_grade(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(id=student_id)
        avg_grade = student.courses_completed.aggregate(Avg('grade_achieved'))['grade_achieved__avg']
        return Response({'average_grade': avg_grade or 0})
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

@api_view(['GET'])
def get_student_ongoing_courses(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(id=student_id)
        courses = student.courses_enrolled.all()
        data = [{
            'id': course.id,
            'name': course.name,
            'department': course.department,
            'description': course.description,
            'remaining_seats': course.remaining_seats
        } for course in courses]
        return Response(data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

@api_view(['GET'])
def get_student_completed_courses(request):
    student_id = request.GET.get('student_id')
    try:
        student = Student.objects.get(id=student_id)
        courses = student.courses_completed.all()
        data = [{
            'id': course.id,
            'name': course.name,
            'department': course.department,
            'description': course.description,
            'grade': course.grade_achieved
        } for course in courses]
        return Response(data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

@api_view(['GET'])
def get_student_course_grade(request):
    student_id = request.GET.get('student_id')
    course_name = request.GET.get('course_name')
    try:
        student = Student.objects.get(id=student_id)
        course = student.courses_completed.get(name=course_name)
        return Response({'grade': course.grade_achieved})
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)
    except CompletedCourse.DoesNotExist:
        return Response({'error': 'Course not found or not completed'}, status=404)