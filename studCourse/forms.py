from django import forms

class CourseForm(forms.Form):
    new_name = forms.CharField()

class DocumentForm(forms.Form):
    new_name = forms.CharField()
    new_media_file = forms.FileField()