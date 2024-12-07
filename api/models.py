from django.db import models

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class CompletedCourse(Course):
    grade_achieved = models.FloatField()

class OngoingCourse(Course):
    remaining_seats = models.IntegerField()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    semester = models.IntegerField()
    courses_enrolled = models.ManyToManyField(OngoingCourse, related_name='enrolled_students')
    courses_completed = models.ManyToManyField(CompletedCourse, related_name='completed_students')

    def __str__(self):
        return self.name