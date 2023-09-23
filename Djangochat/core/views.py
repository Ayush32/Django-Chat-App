from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import SignUpForm 

# Create your views here.

def frontpage(request):
    return render(request, 'core/frontpage.html')

#  signup functionality
def register(request):
    if request.method == 'POST':
        form  = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            login(request,user)
            return redirect('frontpage')
    
    else:
        form = SignUpForm()
        
    return render(request ,'core/register.html',{'form': form})
            