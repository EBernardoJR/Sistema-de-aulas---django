from django import forms

class ContactCourse(forms.Form):#vai gerar um html com o formulário
    name = forms.CharField(label="nome", max_length= 100, required=False)
    email = forms.EmailField(label='E-mail', required=False)
    message = forms.CharField(label="Dúvida", widget=forms.Textarea, required=False)
