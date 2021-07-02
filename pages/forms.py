from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    baslik = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Başlık Giriniz'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email Giriniz'
    }))
    link = forms.URLField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Link Giriniz'
    }))
    aciklama = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Açıklama Giriniz'
    }))
    img = forms.ImageField()


    class Meta:
        model = Contact  #kullanacağım model
        fields = ['baslik', 'email', 'link', 'aciklama', 'img']
        #contact.html'in içine gömerken kullanıcaz

