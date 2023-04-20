from django import forms
from django.forms import ModelForm

from mainapp.models import ProductCategory


class ProductCategoryRegisterForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name',
                  'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # можно назначить стили каждому полю
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
