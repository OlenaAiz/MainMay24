from django import forms
# #from gunicorn.config import User
# from django.contrib.auth.forms import User
from .models import GetInTouch, BookATour


class GetInTouchForm(forms.ModelForm):
    class Meta:
        model = GetInTouch
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'contact-your-name-2', 'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': "contact-email-2", 'placeholder': 'Enter Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'id': "contact-phone-2", 'placeholder': 'Enter Your Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': "contact-message-2", 'placeholder': 'Enter Your Message'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'message': 'Message',
        }
        help_texts = {
            'name': 'Please enter your name its required',
            'email': 'Please enter your email its required',
            'phone': 'Please enter your phone number its required',
            'message': 'Please enter your message its required',
        }
        error_messages = {
            'name': {
                'required': 'This field is required',
            },
            'email': {
                'required': 'This field is required',
            },
            'phone': {
                'required': 'This field is required',
            },
            'message': {
                'required': 'This field is required',
            },
        }


class BookATourForm(forms.ModelForm):
    class Meta:
        model = BookATour
        fields = ('name', 'email', 'phone', 'date', 'count', 'comment')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Phone Number'}),
            'date': forms.DateInput(attrs={'class': 'form-control',
                                           'placeholder': 'Enter Your choosen Date of travel'}),
            'count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter people quantity'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Your comment'}),
        }


# class RegisterForm(forms.ModelForm):
#
#     class Meta:
#         model = User
#         fields = ('username', 'email')
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control'}),
#             'password': forms.PasswordInput(),
#             'email': forms.EmailInput(),
#             'message': forms.Textarea(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#         }
#         labels = {
#            'username': 'Username',
#            'email': 'Email',
#            'phone': 'Phone',
#            'message': 'Message',
#         }
#         help_texts = {
#            'username': 'Це поле є обовязковим',
#            'email': 'Це поле є обовязковим',
#         }
#         error_messages = {
#            'username': {
#                'required':'Це поле є обовязковим',
#            },
#            'email': {
#                'required': 'Це поле є обовязковим',
#            },
#         }
#
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password'])
#         if commit:
#             user.save()
#         return user
