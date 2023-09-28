from django import forms
from django.contrib.auth import authenticate

from .models import CustomUser

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'user_id',
            'username',
            'email',
            'location',
            'groups',
            'password',
            ]
        widgets = {
            "username":   forms.TextInput(attrs={"type":"text","placeholder":"Username"}),
            "email":      forms.EmailInput(attrs={"placeholder":"E-Mail", "required":""}),
            "user_id":    forms.TextInput(attrs={"type":"text","placeholder":"Employee_ID"}),
            "first_name": forms.TextInput(attrs={"type":"text","placeholder":"First Name", "required":""}),
            "last_name":  forms.TextInput(attrs={"type":"text","placeholder":"Last Name", "required":""}),
            "password":   forms.TextInput(attrs={"type":"password","placeholder":"Password"}),
        }
        help_texts = {
            'username': 'Required | 150 characters or fewer | Letters, digits and @/./+/-/_ only.',
            'email': 'Required',
            'password': 'Required',
            'user_id': 'Required',
            'first_name': 'Required',
            'last_name': 'Required',
        }

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name',
            'user_id',
            'username',
            'email',
            'location',
            'groups',
            ]
        widgets = {
            "username":   forms.TextInput(),
            "email":      forms.EmailInput(),
            "user_id":    forms.TextInput(),
            "first_name": forms.TextInput(),
            "last_name":  forms.TextInput(),
        }
        help_texts = {
            'username': 'Required | 150 characters or fewer | Letters, digits and @/./+/-/_ only.',
            'email': 'Required',
            'user_id': 'Required',
            'first_name': 'Required',
            'last_name': 'Required',
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, wrong username or password. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class DeactivateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['is_active',]