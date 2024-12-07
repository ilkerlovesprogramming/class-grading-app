#!/usr/bin/env python
import django
import sys
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'studentgrades.settings')
django.setup()

from api.models import Student, Course, OngoingCourse, CompletedCourse

def setup_data():
    print("Setting up sample data...")
    
    # Create a Course
    course1 = Course.objects.create(
        name="Programming 101",
        code="CS101",
        department="Computer Science",
        description="Introduction to Programming"
    )
    
    ongoing = OngoingCourse.objects.create(
        name="Database Systems",
        code="CS301",
        department="Computer Science",
        description="Introduction to Databases",
        remaining_seats=30
    )
    
    completed = CompletedCourse.objects.create(
        name="Python Programming",
        code="CS201",
        department="Computer Science",
        description="Python Programming",
        grade_achieved=85.5
    )
    
    # Create a Student
    student = Student.objects.create(
        name="John Doe",
        department="Computer Science",
        semester=3
    )
    
    # Add courses to student
    student.courses_enrolled.add(ongoing)
    student.courses_completed.add(completed)
    
    print("\nSetup complete! Verifying data...")
    
    # Verify data
    students = Student.objects.all()
    print(f"\nFound {students.count()} students in database")
    for student in students:
        print(f"\nStudent: {student.name}")
        print("Ongoing courses:", [f"{c.code} - {c.name}" for c in student.courses_enrolled.all()])
        print("Completed courses:", [f"{c.code} - {c.name} (Grade: {c.grade_achieved})" for c in student.courses_completed.all()])

if __name__ == "__main__":
    print("Running database setup and verification...")
    try:
        setup_data()
        print("\nSuccess! Now you can access http://localhost:8000/api/students/ to see the data")
    except Exception as e:
        print(f"\nError: {str(e)}")
        print("\nTroubleshooting steps:")
        print("1. Make sure you've run 'python manage.py migrate'")
        print("2. Ensure the Django server is running")
        print("3. Check database connection settings")