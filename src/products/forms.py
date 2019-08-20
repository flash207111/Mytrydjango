from django import forms


from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='My Title', widget=forms.TextInput(attrs={'placeholder': 'Name product',}))
    # email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'new_class_name two',
        'rows': 20,
        'cols': 100,
        'id_description': 'my-id-description',
        'placeholder': 'Product description',
    }))
    price = forms.DecimalField(initial=99.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" in title:
            raise forms.ValidationError("This is not valid title!")
        return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     if not email.endswith('edu'):
    #         raise forms.ValidationError("email must be a *@*.edu !")
    #     return email

class RawProductForm(forms.Form):
    title = forms.CharField(label='My Title', widget=forms.TextInput(attrs={'placeholder': 'Name product',}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        'class': 'new_class_name two',
        'rows': 20,
        'cols': 100,
        'id_description': 'my-id-description',
        'placeholder': 'Product description',
    }))
    price = forms.DecimalField(initial=99.99)
