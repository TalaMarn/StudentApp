from django.shortcuts import redirect
from functools import wraps

def student_required(view_func):
	@wraps(view_func)
	def wrapped_view(request, *args, **kwargs):
		if not request.session.get('student_id'):
			return redirect('login')
		return view_func(request, *args, **kwargs)

	return wrapped_view

