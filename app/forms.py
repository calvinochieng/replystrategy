from django import forms

class EmailSubmissionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input is-medium',
            'placeholder': 'Enter your email for a discount',
            'required': True
        }),
        label="Your Email",
    )
    # Honeypot field - should remain hidden from users
    birthday = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none;',  # Hidden from user
            'aria-hidden': 'true'
        })
    )
