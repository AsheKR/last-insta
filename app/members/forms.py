from django import forms
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user = None

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                "placeholder": "Username",
                "autofocus": "True",
            },
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )

    def clean(self):
        super().clean()
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is None:
            raise forms.ValidationError('유저 검증에 실패하였습니다')
        self._user = user

    @property
    def user(self):
        if self._user is None:
            raise forms.ValidationError('검증 유저가 존재하지 않습니다.')
        return self._user


