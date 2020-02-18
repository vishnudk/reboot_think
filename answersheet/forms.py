from django import forms


class AnswerSheetUploadForm(forms.Form):
    image = forms.ImageField()

