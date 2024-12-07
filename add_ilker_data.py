import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentgrades.settings')
django.setup()

from api.models import OngoingCourse, CompletedCourse, Student

def create_ilker_data():
    # Create Ilker's courses
    ongoing_courses = [
        {
            'name': 'Application Testing',
            'department': 'CPAN',
            'description': 'CPAN 224 - Application Testing Course',
            'remaining_seats': 30
        },
        {
            'name': 'Principles of Project Management',
            'department': 'CPAN',
            'description': 'CPAN 225 - Project Management Fundamentals',
            'remaining_seats': 30
        },
        {
            'name': 'Network Programming',
            'department': 'CPAN',
            'description': 'CPAN 226 - Network Programming Course',
            'remaining_seats': 30
        },
        {
            'name': 'Advanced Database Programming',
            'department': 'CPAN',
            'description': 'CPAN 227 - Advanced Database Programming Course',
            'remaining_seats': 30
        },
        {
            'name': 'Web Application Development',
            'department': 'CPAN',
            'description': 'CPAN 228 - Web Application Development Course',
            'remaining_seats': 30
        },
        {
            'name': 'Sociology of Cultural Difference',
            'department': 'SOCI',
            'description': 'SOCI 233 - Sociology of Cultural Difference Course',
            'remaining_seats': 30
        },
        {
            'name': 'Career Path Development',
            'department': 'WORK',
            'description': 'WORK 111 - Career Path Development Course',
            'remaining_seats': 30
        }
    ]

    ongoing_course_objects = []
    for course in ongoing_courses:
        oc = OngoingCourse.objects.create(
            name=course['name'],
            department=course['department'],
            description=course['description'],
            remaining_seats=course['remaining_seats']
        )
        ongoing_course_objects.append(oc)

    # Create Ilker's student record
    student = Student.objects.create(
        id=1680555,  # N01680555 without the N0 prefix
        name='Ilker Ozturk',
        department='Computer Programming',
        semester=2  # Winter 2025 would be their second semester
    )

    # Enroll Ilker in all the ongoing courses
    for course in ongoing_course_objects:
        student.courses_enrolled.add(course)

    print(f"Created student record for {student.name} with ID {student.id}")
    print("Enrolled in the following courses:")
    for course in student.courses_enrolled.all():
        print(f"- {course.name} ({course.department})")

if __name__ == '__main__':
    create_ilker_data()