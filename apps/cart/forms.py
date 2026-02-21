from django import forms
from .models import CheckoutForm


class CheckoutModelForm(forms.ModelForm):

    country = forms.ChoiceField(
        choices=[
            ('UZ', 'Uzbekistan'),
            ('KZ', 'Kazakhstan'),
            ('RU', 'Russia'),
            ('US', 'USA'),
        ],
        widget=forms.Select(
            attrs={
                'class': 'form-control form-control-lg rounded-0'
            }
        )
    )

    class Meta:
        model = CheckoutForm
        fields = [
            'name',
            'lastname',
            'email',
            'phone_number',
            'company_name',
            'country',
            'state',
            'city',
            'address_line',
            'street_address'
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your first name'
            }),

            'lastname': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter your last name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'e.g. Jason@example.com'
            }),

            'phone_number': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': '+998 90 123 45 67'
            }),

            'company_name': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Your company name'
            }),

            'state': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),

            'city': forms.TextInput(attrs={
                'class': 'form-control form-control-lg'
            }),

            'address_line': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'House number and street name'
            }),

            'street_address': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Apartment, Suite, Unit, etc (optional)'
            }),
        }