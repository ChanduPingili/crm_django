from django.shortcuts import render  , redirect
from django.contrib.auth import login , logout , authenticate 
from django.contrib import  messages
from .forms import SignUpForm , RecordForm
from .models import Record

def home(request):
  records = Record.objects.all()


  if(request.method == 'POST'):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request , username = username , password = password)
    if user is not None :
      login(request, user)
      messages.success(request , "You are logged in successfully")
      return redirect('home')
    else :
      messages.success(request ,"Invalid username or password")
      return redirect('home')
  else:
    return render(request, 'home.html', {'records':records})
  
def logout_user(request):
  logout(request)
  messages.success(request , "Successfully logged out")
  return redirect('home')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid() :
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username = username , password = password)
      login(request , user)
      messages.success(request , "Registered Successfully")
      return redirect('home')
  else : 
    form = SignUpForm()
    return render(request , 'register.html' , {'form' : form})
  return render(request ,'register.html',{'form' : form} )
      
def customer_record(request, pk):
  if request.user.is_authenticated:
    customer_record = Record.objects.get(id=pk)
    return render(request ,'record.html' , {'customer_record':customer_record} )
  else :
      messages.success(request , "Please login before requesting")

def delete_record(request , pk):
  if request.user.is_authenticated:
    currecord = Record.objects.get(id= pk)
    currecord.delete()
    messages.success(request, f'Delete the recode with id : {pk} Successfully')
    return redirect('home')
  else:
    messages.success(request , "Please login before requesting")
    return redirect('home')

def add_record(request):
  if request.user.is_authenticated:
    form = RecordForm(request.POST or None)
    if request.method == 'POST':
      if form.is_valid():
        form.save()
        messages.success(request , "Record Added Successfully")
        return redirect('home')
      return render(request , 'add_record.html' , {'form' : form})
    else : 
      return render(request , 'add_record.html', {'form':form})
  else : 
      messages.success(request , "You must login to add record")
      return redirect('home')

def update_record(request , pk):
  if request.user.is_authenticated:
    record = Record.objects.get(id=pk)
    form = RecordForm(request.POST or None , instance = record)
    if form.is_valid():
      form.save()
      messages.success(request , 'Record updated successfully')
      return redirect('home')
    return render(request , 'update_record.html' , {'customer_record' : record , 'form' : form})
  else : 
    messages.success(request , 'Login to update the records')
    return redirect('home')
  