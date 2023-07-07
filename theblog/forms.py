from tkinter import Widget
from django  import forms
from .models import post,categorys,Profile
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm,UserCreationForm
from django.contrib.auth.models import User 

choices =  categorys.objects.all().values_list('name','name')

choice_list = []

for item in choices:
	choice_list.append(item)

class add_post_form(forms.ModelForm):
   
    class Meta:
        model = post
        fields=['title','body','category','post_image']

    Widgets = {
        'title':forms.TextInput(attrs={'class': 'form-control'}),
        'body':forms.Textarea(attrs={'class': 'form-control',"Placeholder":choice_list}),
        'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
        



    }



class Edit_settings_Form(UserChangeForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
	username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password')



class password_change_form(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:    
        model = User
        fields = ('old_password','new_password1','new_password2')
		


class ProfilePage_Form(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'pinterest_url')

		
		widgets = {
			'bio': forms.Textarea(attrs={'class': 'form-control'}),
			#'profil_pic': forms.TextInput(attrs={'class': 'form-control'}),
			'website_url': forms.TextInput(attrs={'class': 'form-control', }),
			'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
			'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
			'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),			
			'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),			
		}
    
class SignUpForm(UserCreationForm):  
    email = forms.EmailField(max_length=200, help_text='Required')  
    class Meta:  
        model = User  
        fields = ('username', 'email', 'password1', 'password2')  










#class SignUpForm(UserCreationForm):
#	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#	first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#	last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

#	class Meta:
#		model = User
#		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


	#def __init__(self, *args, **kwargs):
	#	super(SignUpForm, self).__init__(*args, **kwargs)

	#	self.fields['username'].widget.attrs['class'] = 'form-control'
	#	self.fields['password1'].widget.attrs['class'] = 'form-control'
	#	self.fields['password2'].widget.attrs['class'] = 'form-control'


    


