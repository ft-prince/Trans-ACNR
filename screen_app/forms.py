from django import forms
from .models import Screen, PDFFile, VideoFile

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = ['manager', 'product', 'upload_pdf', 'upload_video']
        widgets = {
            'upload_pdf': forms.CheckboxSelectMultiple(),
            'upload_video': forms.CheckboxSelectMultiple(),
        }

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['pdf_duration', 'pdf_name', 'pdf_file']

class VideoFileForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = ['video_duration', 'video_name', 'video_file']