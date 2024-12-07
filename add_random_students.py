import os
import django
import random
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentgrades.settings')
django.setup()

from api.models import Student, OngoingCourse, CompletedCourse

def generate_random_name():
    first_names = ['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Ethan', 'Sophia', 'Mason', 'Isabella', 'William']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def create_random_students(num_students=5):
    # Get Ilker's ongoing courses
    ilker = Student.objects.get(name='Ilker Ozturk')
    ilker_courses = ilker.courses_enrolled.all()
    
    # Create random students
    for i in range(num_students):
        # Create student with random name
        student = Student.objects.create(
            name=generate_random_name(),
            department='Computer Programming',  # Same as Ilker
            semester=2  # Same semester as Ilker
        )
        
        # Enroll in same courses as Ilker
        for course in ilker_courses:
            student.courses_enrolled.add(course)
            
            # Also create a completed version of some courses with random grades
            if random.random() > 0.5:  # 50% chance to have completed a version of this course
                completed_course = CompletedCourse.objects.create(
                    name=course.name,
                    department=course.department,
                    description=course.description,
                    grade_achieved=random.uniform(60.0, 95.0)  # Random grade between 60 and 95
                )
                student.courses_completed.add(completed_course)
        
        print(f"Created student: {student.name}")
        print("Enrolled courses:")
        for course in student.courses_enrolled.all():
            print(f"- {course.name}")
        print("Completed courses:")
        for course in student.courses_completed.all():
            print(f"- {course.name} (Grade: {course.grade_achieved:.1f})")
        print()

if __name__ == '__main__':
    create_random_students()