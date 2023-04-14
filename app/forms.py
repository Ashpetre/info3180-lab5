# Add any form classes for Flask-WTF here
from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(label='Movie Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'rows': 3}))
    poster = forms.ImageField(label='Movie Poster', help_text='Only images of movie posters are allowed')

    def clean_poster(self):
        poster = self.cleaned_data.get('poster', False)
        if poster:
            if poster.content_type not in ['image/jpeg', 'image/png']:
                raise forms.ValidationError("Invalid file format. Only JPEG and PNG images are allowed.")
            if poster.size > 2 * 1024 * 1024:
                raise forms.ValidationError("File size too large. Maximum file size allowed is 2MB.")
        else:
            raise forms.ValidationError("Please upload an image of the movie poster.")
        return poster
    



