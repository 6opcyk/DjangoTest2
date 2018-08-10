from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
	use_in_migrations = True
	def create_user(self, email, password, **fields):
		email = self.normalize_email(email)
		user = self.model(email=email, **fields)
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, email, password, **fields):
		fields['is_superuser'] = True
		fields['is_staff'] = True
		user = self.create_user(email, password, **fields)
		user.save()
		return user

class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	first_name = models.CharField(max_length = 120)
	last_name = models.CharField(max_length = 120)
	date_joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	
	eth_token = models.CharField(max_length = 120, default = "None")
	eth_adress = models.CharField(max_length = 120, default = "None")

	objects = UserManager()

	USERNAME_FIELD = 'email'

	def get_full_name(self):
		full_name = f'{self.first_name} {self.last_name}' 
		return full_name

	def get_short_name(self):
		return self.first_name

