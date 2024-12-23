from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
  email = forms.EmailField(label='', widget=forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Enter email'}) )
  first_name = forms.CharField(label = '', max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter first name'}))
  last_name = forms.CharField(label = '',max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder' : 'Enter last name'}))

  class Meta:
    model = User
    fields = ('username' , 'email', 'first_name', 'last_name' , 'password1', 'password2')

  def __init__(self , *args , **kwargs):
    super(SignUpForm, self).__init__(*args, **kwargs)

    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'Enter username'
    self.fields['username'].label = ''
    self.fields['username'].helptext = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
    
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    self.fields['password1'].label = ''
    self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    self.fields['password2'].label = ''
    self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


class RecordForm(forms.ModelForm):
  first_name = forms.CharField(max_length=50 ,label='' , widget=forms.TextInput(attrs={'placeholder':'Enter your First Name' , 'class':'form-control'}))
  last_name = forms.CharField(max_length=50 ,label='' , widget=forms.TextInput(attrs={'placeholder':'Enter your Last Name' , 'class':'form-control'}))
  email = forms.EmailField(label='', widget=forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Enter your Email'}) )
  phone = forms.CharField(label='',max_length=20, widget=forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Enter your Phone Number'}) )
  address = forms.CharField(max_length=50 ,label='' , widget=forms.TextInput(attrs={'placeholder':'Enter your Address' , 'class':'form-control'}))
  state = forms.CharField(max_length=50 ,label='' , widget=forms.TextInput(attrs={'placeholder':'Enter your Statte' , 'class':'form-control'}))
  city = forms.CharField(max_length=50 ,label='' , widget=forms.TextInput(attrs={'placeholder':'Enter your City' , 'class':'form-control'}))
  zipcode = forms.CharField(max_length=50 ,label='' , widget=forms.TextInput(attrs={'placeholder':'Enter your Zip Code' , 'class':'form-control'}))

  class Meta:
    model = Record
    exclude = ("user",)