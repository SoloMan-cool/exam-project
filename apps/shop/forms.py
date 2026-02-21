from django import forms
from .models import ProductReview

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReview
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Enter your review',
            })
        }