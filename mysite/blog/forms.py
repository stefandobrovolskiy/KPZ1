from django import forms
from .models import ArticleImage

class MultiImageInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # ось ця магія дозволяє multiple

class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=MultiImageInput(attrs={'multiple': True})
    )

    class Meta:
        model = ArticleImage
        fields = '__all__'
