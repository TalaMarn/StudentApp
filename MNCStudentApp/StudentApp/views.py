from django.shortcuts import redirect, render
from .decorators import student_required
from .models import Student
from .forms import LoginForm
# Create your views here.

def login_view(request):
	form = LoginForm()
	
@student_required
def student_list(request):
	students = Student.objects.all()
	return render(request, 'student_list.html', {'students': students})
