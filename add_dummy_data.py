import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentgrades.settings')
django.setup()

from api.models import Student, OngoingCourse, CompletedCourse

def create_dummy_data():
    # Create Ongoing Courses
    ongoing_courses = [
        {
            'name': 'Introduction to Python',
            'department': 'Computer Science',
            'description': 'Basic Python programming concepts',
            'remaining_seats': 15
        },
        {
            'name': 'Web Development',
            'department': 'Computer Science',
            'description': 'HTML, CSS, and JavaScript fundamentals',
            'remaining_seats': 10
        },
        {
            'name': 'Database Management',
            'department': 'Information Technology',
            'description': 'SQL and database design',
            'remaining_seats': 20
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

    # Create Completed Courses
    completed_courses = [
        {
            'name': 'Mathematics 101',
            'department': 'Mathematics',
            'description': 'Basic calculus and algebra',
            'grade': 85.5
        },
        {
            'name': 'Physics Fundamentals',
            'department': 'Physics',
            'description': 'Introduction to physics concepts',
            'grade': 92.0
        },
        {
            'name': 'English Composition',
            'department': 'English',
            'description': 'Essay writing and grammar',
            'grade': 88.5
        }
    ]

    completed_course_objects = []
    for course in completed_courses:
        cc = CompletedCourse.objects.create(
            name=course['name'],
            department=course['department'],
            description=course['description'],
            grade_achieved=course['grade']
        )
        completed_course_objects.append(cc)

    # Create Students
    students = [
        {
            'name': 'John Doe',
            'department': 'Computer Science',
            'semester': 3
        },
        {
            'name': 'Jane Smith',
            'department': 'Information Technology',
            'semester': 4
        },
        {
            'name': 'Bob Johnson',
            'department': 'Computer Science',
            'semester': 2
        }
    ]

    for student_data in students:
        student = Student.objects.create(
            name=student_data['name'],
            department=student_data['department'],
            semester=student_data['semester']
        )
        # Add some ongoing courses to each student
        for course in ongoing_course_objects[:2]:
            student.courses_enrolled.add(course)
        
        # Add some completed courses to each student
        for course in completed_course_objects[:2]:
            student.courses_completed.add(course)

if __name__ == '__main__':
    print("Creating dummy data...")
    create_dummy_data()
    print("Dummy data created successfully!")
