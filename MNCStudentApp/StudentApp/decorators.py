from django.shortcuts import redirect
from functools import wraps
from .models import Profile

def student_required(view_func):
	@wraps(view_func)
	def _wrapped_view(request, *args, **kwargs):
		is_student = (
			request.user.is_authenticated
			and Profile.objects.filter(user_id=request.user.username, role='student').exists()
		)
		if is_student:
			return view_func(request, *args, **kwargs)
		else:
			return redirect('login')  # Redirect to login page if not a student
	return _wrapped_view