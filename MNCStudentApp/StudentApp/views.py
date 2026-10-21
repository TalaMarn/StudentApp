from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import LoginForm
from .models import Profile


def login_view(request):
	form = LoginForm(request.POST if request.method == 'POST' else None)

	if request.method == 'POST' and form.is_valid():
		user_id = form.cleaned_data['user_id']
		password = form.cleaned_data['password']
		profile = Profile.objects.filter(
			user_id=user_id,
			password=password,
		).first()

		if profile is not None:
			user, created = User.objects.get_or_create(
				username=profile.user_id,
				defaults={'email': profile.email},
			)
			if created or not user.check_password(password):
				user.set_password(password)
				user.save(update_fields=['password'])
			login(request, user)
			return redirect('student_list')

		return render(
			request,
			'login.html',
			{'form': form, 'error': 'Invalid user ID or password.'},
		)

	return render(request, 'login.html', {'form': form})


def student_list(request):
	students = Profile.objects.filter(role='student')
	return render(request, 'student_list.html', {'students': students})
