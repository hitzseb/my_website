from django import forms

class ContactForm(forms.Form):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    Email = forms.EmailField()
    Asunto = forms.CharField()
    Mensaje = forms.CharField(widget=forms.Textarea)