from django.db import models

# Create your models here.

class Student(models.Model):
    student_id = models.TextField(primary_key=True)
    full_name = models.TextField()
    email = models.TextField()

    def __str__(self):
        return self.full_name

class Course(models.Model):
    course_id = models.TextField(primary_key=True)
    course_name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    grade =models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.full_name} enrolled in {self.course.course_name}"

class Schedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.course_name} - {self.day_of_week} {self.start_time} to {self.end_time}"