from django import forms
from myapp.models import * 


# Song form class
class SongForm(forms.ModelForm):
    song_name = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'Enter Song Name'}))	        

    duration = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'Enter Duration Name'}))	        

   
    class Meta:
        model = Song
        fields = ['song_name', 'duration']

# Podcast form class
class PodcastForm(forms.ModelForm):
    podcast_name = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'Enter Podcast Name'}))	        

    duration = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'Enter Duration Time'}))

    host = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control','placeholder':'Enter Host Name'})) 

    participants = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control','placeholder':'Enter Participants'}))        	        
       	        

    class Meta:
        model = Podcast
        fields = ['podcast_name', 'duration', 'host', 'participants']   

# Audiobook form class
class AudioBookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'Enter Title'}))	        

    author = forms.CharField(widget=forms.TextInput
        (attrs={'class':'form-control','placeholder':'Enter Author name'}))

    narrator = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control','placeholder':'Enter Narrator'})) 

    duration = forms.CharField(widget=forms.TextInput
    (attrs={'class':'form-control','placeholder':'Enter Duration'}))        	        
       	        

    class Meta:
        model = AudioBook
        fields = ['title', 'author', 'narrator', 'duration']                
