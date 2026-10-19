from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .decorators import student_required
from .models import Profile
from .forms import LoginForm
# Create your views here.

def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user_id = form.cleaned_data['usern_id']
			password = form.cleaned_data['password']
			user = authenticate(request, username=user_id, password=password)
			if user is not None:
				login(request, user)
				return redirect('student_list')  # Redirect to student list after successful login
			else:
				return redirect('login')
	else:
		return render(request, 'login.html', {'form': LoginForm()})

	
@student_required
def student_list(request):
	students = Profile.objects.filter(role='student')
	return render(request, 'student_list.html', {'students': students})