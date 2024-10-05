from django.db import models

class StudentDetails(models.Model):
    studentName = models.CharField('Student Name', max_length=30)
    studentEmail = models.EmailField('Email ID', max_length=40)
    studentPassword = models.CharField('Password', max_length=14)
    studentRegNo = models.CharField('Reg.no', max_length=9)
    studentGender = models.CharField('Gender', max_length=6)

    def __str__(self):
        return f"The student: {self.studentRegNo}"

class TeacherDetails(models.Model):
    teacherName = models.CharField('Teacher Name', max_length=30)
    teacherEmail = models.EmailField('Email ID', max_length=40)
    teacherPassword = models.CharField('Password', max_length=14)
    teacherGender = models.CharField('Gender', max_length=6)

    def __str__(self):
        return f"The Teacher: {self.teacherName}"

class QueryDetails(models.Model):
    studentIdInQuery = models.IntegerField('Student Id', default=0)
    courseInQuery = models.CharField('Course Name', max_length=50)
    courseCodeInQuery = models.CharField('Course Code', max_length=10)
    slotInQuery = models.CharField('Slot', max_length=10)
    topicInQuery = models.CharField('Topic', max_length=50)
    doubtInQuery = models.TextField('Query')
    feedbackInQuery = models.TextField('Reply',default='Not Replied...')
    feedbackStatus = models.CharField('Feedback status', max_length=1, default='N')

    def __str__(self):
        return f"The query: {self.id}"

