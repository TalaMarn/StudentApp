from django.test import TestCase
from django.contrib.auth.models import User
from django.test import RequestFactory
from .models import Profile
from .decorators import student_required


class ProfileTests(TestCase):
	def test_initial_password_defaults_to_user_id(self):
		profile = Profile.objects.create(
			user_id='student001',
			full_name='Test Student',
			email='student@example.com',
		)

		self.assertEqual(profile.password, 'student001')


class StudentRequiredTests(TestCase):
	def setUp(self):
		self.factory = RequestFactory()

	def test_authenticated_student_is_allowed_without_profile_relation(self):
		user = User.objects.create_user(username='student001', password='student001')
		Profile.objects.create(
			user_id='student001',
			full_name='Test Student',
			email='student@example.com',
		)
		request = self.factory.get('/')
		request.user = user

		protected_view = student_required(lambda request: 'allowed')

		self.assertEqual(protected_view(request), 'allowed')
