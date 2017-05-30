from django import forms


class LoginForm(forms.Form):

    name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    nick_name = forms.CharField(
        label='ニックネーム',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    password = forms.CharField(
        label='パスワード',
        max_length=20,
        required=True,
        widget=forms.PasswordInput()
    )