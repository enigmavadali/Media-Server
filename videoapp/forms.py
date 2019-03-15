from django import forms
from .models import Document, Lecture,Comment
# class DocumentForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput())
#     description = forms.CharField(widget=forms.TextInput())
#     docfile = forms.FileField()
#
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     description = forms.CharField(widget=forms.TextInput())
#     file = forms.FileField()


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'tag','description','docfile']

class LectureForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type' : 'date', 'value' : '01/01/2019'}))
    antim_tarikh = forms.DateField(label="End Date",widget=forms.widgets.DateInput(attrs={'type' : 'date', 'value' : '01/01/2019'}))
    class Meta:
        model = Lecture
        fields = ['title','start_date','start_hour','start_min','antim_tarikh','end_hour','end_min','tag','docfile']


# class CommentForm(forms.ModelForm):
#     # comment = forms.TextInput()
#     class Meta:
#         model = Comment
#         fields = ['body']

class CommentForm(forms.ModelForm):
   # comment = forms.TextInput()
   body = forms.CharField(widget=forms.TextInput(attrs={'class':'text-line'}), label='')
   class Meta:
       model = Comment
       fields = ['body']
