from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Input your Name',
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Input your Password',
            }
        ))
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Input your Password',
            }
        )
    )
    agree = forms.BooleanField(
        label='Agree',
        widget=forms.CheckboxInput(
            attrs={
                'class':'form-check-input',
            }
        )
    )
