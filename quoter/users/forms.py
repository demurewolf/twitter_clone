
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import Profile

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2', # Password consistency check
        ]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'nickname',
            'birth_date',
            'bio',
            'location',
        ]