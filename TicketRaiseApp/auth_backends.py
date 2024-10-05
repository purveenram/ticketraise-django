from django.contrib.auth.backends import ModelBackend
from .models import StudentDetails

class StudentAuthBackend(ModelBackend):
    def authenticate(self, request, studentEmail=None, studentPassword=None):
        try:
            user = StudentDetails.objects.get(studentEmail=studentEmail)
            if user.studentPassword == studentPassword:
                return user
        except StudentDetails.DoesNotExist:
            return None
