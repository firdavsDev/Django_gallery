from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.decorators import login_required #oldin login bajariladi sung profile/ utadi sittings.py ----> LOGIN_URL = 'login'  qushish kerak 

#from django.contrib.auth.forms import UserCreationForm #registratsiyadan utish uchun tayor

from django.contrib import messages

from .forms import UserregisterForm

# Create your views here.
def rigester(request):
    if request.method == 'POST':
        form = UserregisterForm(request.POST) #html ichidagi malumotlarni oladi uziga
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'{username} akounti yaratildi! Login bo\'lib kirishingiz mumkin!!!')
            return redirect('login')
    else:
        form = UserregisterForm()
    return render(request, 'users/rigester.html',{'form':form})

