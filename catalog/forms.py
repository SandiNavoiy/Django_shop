
from django import forms
from django.forms import formset_factory

from .models import Product, Category, Version
class VersionForm(forms.ModelForm):

    class Meta:
        """подкласс описания """
        model = Version  # модель
        fields = '__all__'  # поля



class ProductForm(forms.ModelForm):


    class Meta:
        """подкласс описания """
        model = Product  # модель
        fields = '__all__'  # поля

        def save(self, commit=True):
            instance = super().save(commit=False)
            instance.user = self.request.user
            if commit:
                instance.save()
            return instance


    def clean_product_name(self):
        """метод валидации по запрерщенным словам"""
        cleaned_data = self.cleaned_data.get('product_name')
        if cleaned_data in (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"):
            raise forms.ValidationError('Запрещенное слово')
        return cleaned_data

    def clean_description_product(self):
        """метод валидации по заперщенным словам"""
        cleaned_data = self.cleaned_data.get('description_product')
        if cleaned_data in (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"):
            raise forms.ValidationError('Запрещенное слово')
        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        """подкласс описания """
        model = Category  # модель
        fields = '__all__'  # поля

    def clean_category_name(self):
        """метод валидации по запрерщенным словам"""
        cleaned_data = self.cleaned_data.get('category_name')
        if cleaned_data in (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"):
            raise forms.ValidationError('Запрещенное слово')
        return cleaned_data

    def clean_description_category(self):
        """метод валидации по заперщенным словам"""
        cleaned_data = self.cleaned_data.get('description_category')
        if cleaned_data in (
        "казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"):
            raise forms.ValidationError('Запрещенное слово')
        return cleaned_data
