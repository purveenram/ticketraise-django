from django import forms
from .models import *

class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields =  ['studentName', 'studentEmail','studentPassword','studentRegNo','studentGender']

class TeacherDetailsForm(forms.ModelForm):
    class Meta:
        model = TeacherDetails
        fields =  ['teacherName', 'teacherEmail','teacherPassword','teacherGender']
    
class QueryDetailsForm(forms.ModelForm):
    class Meta:
        model = QueryDetails
        fields =  ['studentIdInQuery', 'courseInQuery','courseCodeInQuery','slotInQuery','topicInQuery','doubtInQuery','feedbackInQuery','feedbackStatus']

